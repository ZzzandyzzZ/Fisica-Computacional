import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import math as mt
from time import time
from matplotlib.animation import FuncAnimation,PillowWriter


c=200
img=[]
a=np.random.randint(2, size=c)
b=np.empty(c)
j=c-1
#plt.axis([0, c,0, c])
#print(a)
while (j>=0):
    for i in range(c):
        l=i-1
        r=i+1
        if(l<=-1):
            l=c-1
        if(r>=c):
            r=0
        al=a[l]
        ar=a[r]
        if (al==1 and a[i]==1 and ar==1) :
            b[i]=0
        if (al==1 and a[i]==1 and ar==0):
            b[i]=1
        if (al==1 and a[i]==0 and ar==1 ):
            b[i]=1
        if (al==1 and a[i]==0 and ar==0 ):
            b[i]=0
        if (al==0 and a[i]==1 and ar==1) :
            b[i]=0
        if (al==0 and a[i]==1 and ar==0) :
            b[i]=0
        if (al==0 and a[i]==0 and ar==1 ):
            b[i]=0
        if (al==0 and a[i]==0 and ar==0 ):
            b[i]=1
        """
        if (al==1 and a[i]==1 and ar==1) :
            b[i]=0
        if (al==1 and a[i]==1 and ar==0):
            b[i]=1
        if (al==1 and a[i]==0 and ar==1 ):
            b[i]=1
        if (al==1 and a[i]==0 and ar==0 ):
            b[i]=0
        if (al==0 and a[i]==1 and ar==1) :
            b[i]=0
        if (al==0 and a[i]==1 and ar==0) :
            b[i]=1
        if (al==0 and a[i]==0 and ar==1 ):
            b[i]=1
        if (al==0 and a[i]==0 and ar==0 ):
            b[i]=1
        """
    img.append(b.copy())
    #print(b)
    a=b
    j=j-1
#print(img)
#plt.imshow(img,vmin=0,vmax=1)
#plt.show()
#print(img)
def drawPoints(i):
    print(i)
    #print(img[:i+1])
    plt.clf()
    plt.imshow(img[:i+1],vmin=0,vmax=1)

fig, axs = plt.subplots()

ani= FuncAnimation(fig,drawPoints,range(0,c),interval=100)
#plt.show()
print("CREANDO")
writergif = PillowWriter(fps=60)
ani.save('animation.gif')
print("TERMINO")