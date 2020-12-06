import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math as mt
from time import time
from matplotlib.animation import FuncAnimation,PillowWriter
def MonteCarlo(fun1,fun2=lambda x,y:True):
    sa = 0
    saa = 0
    start=time()
    for k in range(veces):
        n=0
        px=[]
        py=[]
        for i in range(m):
            r=rd.random()
            x = ax + (bx-ax)*r
            r=rd.random()
            y = ay + (by-ay)*r
            if(fun1(x,y) and fun2(x,y)):
                n+=1
                px.append(x)
                py.append(y)
        area = n*(by-ay)*(bx-ax)/m
        sa = sa + area
        saa = saa + area**2
    finish=time()
    prom = sa/veces
    desv = mt.sqrt(veces*saa-sa**2)/veces
    promedio = str(prom)
    desviacion = str(desv)
    """
    plt.scatter(px,py,0.5,label=
    'promedio={:.4}\ndesviacion=+-{:.4}\ntiempo={:.4f}'.format(
    promedio,desviacion,finish-start))
    plt.title('Areas por el metodo MonteCarlo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().axis('equal')
    plt.legend()
    plt.show()
    """
    return px,py
def MonteCarlo3D(fun1,fun2=lambda x,y:True):
    sa = 0
    saa = 0
    start=time()
    for k in range(veces):
        n=0
        px=[]
        py=[]
        pz=[]
        for i in range(m):
            r=rd.random()
            x = ax + (bx-ax)*r
            r=rd.random()
            y = ay + (by-ay)*r
            r=rd.random()
            z = az + (bz-az)*r
            if(fun1(x,y,z) and fun2(x,y)):
                n+=1
                px.append(x)
                py.append(y)
                pz.append(z)
        area = n*(by-ay)*(bx-ax)*(bz-az)/m
        sa = sa + area
        saa = saa + area**2
    finish=time()
    prom = sa/veces
    desv = mt.sqrt(veces*saa-sa**2)/veces
    promedio = str(prom)
    desviacion = str(desv)
    fig = plt.figure()
    axs = fig.add_subplot(111, projection='3d')
    axs.scatter(px,py,pz,s=0.5,label=
    'promedio={:.4}\ndesviacion=+-{:.4}\ntiempo={:.4f}'.format(
    promedio,desviacion,finish-start))
    plt.title('Areas por el metodo MonteCarlo')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
#Numero de puntos
m=100000
#Iteraciones
veces=50
#Limites
ax = 0
bx = 2
ay = -4
by = 0
az= -9
bz= -0.2
#Funcion para determinar que puntos se usaran
#MonteCarlo(lambda x,y:y<=mt.exp(-x**2))
#MonteCarlo(lambda x,y:y**2<=2*x+1, lambda x,y:y>=x-1)
#MonteCarlo3D(lambda x,y,z:x**2/2+y**2/3+z**2/4<=1)
#MonteCarlo3D(lambda x,y,z:z<=mt.sin(x)*mt.cos(y-mt.pi))
#MonteCarlo3D(lambda x,y,z:z<=(2*y-1)/(2*x+1),lambda x,y:2*x-y>=4)
"""
start=time()

for k in range(veces):
    n=0
    px=[]
    py=[]
    for i in range(m):
        r=rd.random()
        x = ax + (bx-ax)*r
        r=rd.random()
        y = ay + (by-ay)*r
        if (y<=mt.exp(-x**2)):
        #if(y<=sqrt(x) && y>=x^2)
        #if(y>=x-1 and y**2<=2*x+1):
        #if(x**2/4+y**2/9<1):
            n+=1
            px.append(x)
            py.append(y)
    area = n*(by-ay)*(bx-ax)/m
    sa = sa + area
    saa = saa + area**2
finish=time()
prom = sa/veces
desv = mt.sqrt(veces*saa-sa**2)/veces
promedio = str(prom)
desviacion = str(desv)
plt.scatter(px,py,0.5,label=
'promedio={:.4}\ndesviacion=+-{:.4}\ntiempo={:.4f}'.format(
promedio,desviacion,finish-start))
plt.title('Areas por el metodo MonteCarlo')
plt.xlabel('x')
plt.ylabel('y')
plt.gca().axis('equal')
plt.legend()
plt.show()
"""
def drawPoints(i):
    plt.scatter(px[i:i+100],py[i:i+100],0.5)
ax = 0
bx = 1
ay = 0
by = 1
fig, axs = plt.subplots()
axs.set_ylim(ax,bx)
axs.set_xlim(ay,by)
px,py=MonteCarlo(lambda x,y:y>=x**2, lambda x,y:y<=mt.sqrt(x))
ani= FuncAnimation(fig,drawPoints,range(0,len(px),100),interval=10)
#plt.show()
print("CREANDO")
writergif = PillowWriter(fps=60)
ani.save('animation.gif')
print("TERMINO")
