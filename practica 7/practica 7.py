import numpy as np
import random as r
import math as ma
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
def feval(funcName, *args):
    return eval(funcName)(*args)
#f = lambda x:x**2-x+np.sin(2*np.pi*x)
f = lambda x: 2*x if(0<=x<=1/2) else 2-2*x
g=lambda y:0
x=None
y=None
U=None
##def f(x):
##    if(0<=x<=1/2):
##        return 2*x
##    if(1/2<=x<=1):
##        return 2-2*x
def animar(i):
    h=0.05
    #print(i)
    plt.gca().clear()
   # print("Animacion",x.shape,y.shape,U[:,i].shape)
    plt.gca().plot(np.arange(0,len(U[:,i])),U[:,i])
   
    #plt.gca().plot(x[0],U[i])
def graficar(U,titulo):
    global x,y
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(titulo)
    x, y = np.meshgrid(y,x)
    print(x.shape,y.shape,U.shape)
    surf=ax.plot_surface(x, y,U, alpha=0.9, cmap=cm.coolwarm,linewidth=1, antialiased=False)
    cset = ax.contourf(x, y, U, zdir='z', offset=np.min(U), cmap=cm.coolwarm)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
    print(U)
def onda(a,b,v,h,k):
    global x,y,U
    x=np.arange(0,a+h,h)
    y=np.arange(0,b+k,k)
    n=len(x)
    m=len(y)
    r=v*k/h
    print(r,k/h)
    print(m,n)
    r1=r**2;
    r2=r**2/2;
    s1=1-r**2;
    s2=2*(1-r**2);
    U=np.zeros((n,m));
    for i in range(2,n):
        #print("I",i)
        U[i-1,0]=feval('f',h*(i-1));
        #print(h*(i-1))
        U[i-1,1]=s1*feval('f',h*(i-1))+k*feval('g',h*(i-1))+r2*(feval('f',h*i)+feval('f',h*(i-2)));
    #print(U)
    for j in range(1,m-1):
       # print("J",j)
        for i in range(1,n-1):
            U[i,j+1]= s2*U[i,j]+r1*(U[i-1,j]+U[i+1,j])-U[i,j-1];
    #graficar(U,'Onda')
onda(1,1,1,0.04,0.03)
#onda(1,1,4,0.03,0.01)
#onda(1,1,5,0.09,0.01)
#onda(1,1,2,0.05,0.01)
x, y = np.meshgrid(y,x)
#plt.xlim([-5, -5])
plt.ylim(0, 1)
ani =animation.FuncAnimation(plt.gcf(),animar,range(0,U.shape[1]),interval=10,repeat_delay =1000)
#graficar(U,'Onda')
plt.show()
