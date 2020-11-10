import numpy as np
import random as r
import math as ma
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
I=None
J=None
All=[]
B=[]
A=[]
x=None
y=None
m=None
n=None
def pos(i,j):
    return (i-1)*(n-2)+j-1
def comprobar(U,i,j):
    if(U[i,j]!=None):
        B[pos(I,J),0]+=U[i,j]
    else:
        A[pos(I,J),pos(i,j)]=-1
def feval(funcName, *args):
    return eval(funcName)(*args)
def animar(i):
    plt.gca().clear()
    surf=plt.gca().plot_surface(x, y,All[i], alpha=0.9, cmap=cm.coolwarm,linewidth=1, antialiased=False)
    cset = plt.gca().contourf(x, y, All[i], zdir='z', offset=np.min(All[i]), cmap=cm.coolwarm)
def graficar(U,titulo):
    global x,y
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(titulo)
    x, y = np.meshgrid(y,x)
    surf=ax.plot_surface(x, y,U, alpha=0.9, cmap=cm.coolwarm,linewidth=1, antialiased=False)
    cset = ax.contourf(x, y, U, zdir='z', offset=np.min(U), cmap=cm.coolwarm)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
def inicializar(a,b,h):
    global x,y,m,n,f,c
    m=int(a/h)+1
    n=int(b/h)+1
    f=int((m-1)*h)
    c=int((n-1)*h)
    x=np.arange(0,f+h,h)
    y=np.arange(0,c+h,h)
def gauss(a,b,h):
    global m,n,B,A,I,J,x,y
    inicializar(a,b,h)
    v=(m-2)*(n-2)
    B=np.full([v,1], 0)
    X=np.full([v],0)
    A=np.full([v, v], 0)
    U=crear_matriz(h,'gauss')
    for i in range(1,U.shape[0]-1):
        for j in range(1,U.shape[1]-1):
            I=i
            J=j
            A[pos(i,j),pos(i,j)]=4
            comprobar(U,i,j-1)
            comprobar(U,i,j+1)
            comprobar(U,i-1,j)
            comprobar(U,i+1,j)
    X=np.linalg.solve(A,B)
    X=np.reshape(X,(m-2,n-2))
    X=crear_matriz(h,'g_resuelto',X)
    graficar(X,'Solucion con Gauss')
def crear_matriz(h,op,X=None):
    if(op=='gauss'):
        U= np.full([m, n], None)
    elif(op=='rapido'):
        a=int((m-1)*h)
        b=int((n-1)*h)
        pp=(a*(feval('f1',0)+feval('f2',0))+
            b*(feval('f3',0)+feval('f4',0)))/(2*a+2*b);
        U=np.ones((m,n))*0.9*pp
    elif(op=='aleatorio'):
        U=np.random.randint(300, size=(m,n))
    elif(op=='g_resuelto'):
        U= np.full([m, n], None)
        for i in range(X.shape[0]):
            U[i+1,1:n-1]=X[i]
    else: return None
    print(U[0,:])
    print(feval('f3',y))
    U[0,:]=feval('f3',y)
    U[:,0]=feval('f1',x)
    U[-1,:]=feval('f4',y)
    U[:,-1]=feval('f2',x)
    U[0,0]=(U[0,1]+U[1,0])/2
    U[0,-1]=(U[0,-2]+U[1,-1])/2
    U[-1,0]=(U[-2,0]+U[-1,1])/2
    U[-1,-1]=(U[-2,-1]+U[-1,-2])/2
    return U
f1 = lambda y:20
f2=lambda y:300
f3 =lambda x:80
f4=lambda x:0

f1 = lambda x:x**2
f2=lambda x:(x-1)**2
f3 =lambda x:x**2
f4=lambda x:(x-2)**2
def laplace_i(a,b,h,epsilon):
    global x,y,m,n
    inicializar(a,b,h)
    U=crear_matriz(h,'rapido')
    #U=crear_matriz(h,'aleatorio')
    w=4/(2+ma.sqrt(4-(ma.cos(np.pi/(m-1))+ma.cos(np.pi/(n-1)))**2));
    rmax=1;
    while(rmax>epsilon):
        rmax=0
        for i in range(1,m-1):
            for j in range(1,n-1):
                rij=(U[i,j+1]+U[i,j-1]+U[i+1,j]+U[i-1,j]-4*U[i,j])/4;
                U[i,j]=U[i,j]+w*rij;
                if rmax<=abs(rij):
                    rmax=abs(rij);
        All.append(U.copy())
    graficar(U,'Solucion iterativa')
laplace_i(2,1,0.05,0.01)
##plt.gcf().gca(projection='3d')
##ani =animation.FuncAnimation(plt.gcf(),animar,range(0,len(All)),interval=1000)
##
gauss(2,1,0.05)


def fnc(X):
    return (X[0] - X[1]) ** 2

fig = plt.figure()
ax = fig.add_subplot(111, projection=Axes3D.name)
X, Y = np.meshgrid(x,y)
Z = fnc([X,Y])
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.view_init(elev=15, azim=-118)
plt.show()
