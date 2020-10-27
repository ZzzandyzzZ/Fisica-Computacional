import matplotlib.pyplot as plt
import random as ra
import numpy as np
from numpy import array as npa
import matplotlib.animation as animation
import matplotlib.patches as mp
def euler(espacio,velocidad):
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    pt = np.arange(0,time,h)
    pe=[]
    for t in pt:
        aceleracion=(-espacio/(sum(espacio**2))**(1.5))
        velocidad+=(aceleracion*h)
        espacio+=(velocidad*h)
        if(abs(espacio[0])>xlim):break
        if(abs(espacio[1])>ylim):break
        if((sum(espacio**2))**0.5<=r):break
        pe.append(espacio.tolist())
    return npa(pe)
def tres_cps(espacio,velocidad):
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    aceleracion = npa([0,0],dtype=np.float32)
    pt = np.arange(0,time,h)
    pe=[]
    pv=[]
    pa=[]
    for t in pt:
        x1=espacio[0]+d
        x2=espacio[0]-d
        y=espacio[1]
        aceleracion[0]=-x1/(x1**2+y**2)**(1.5)-x2/(x2**2+y**2)**(1.5)
        aceleracion[1]=-y/(x1**2+y**2)**(1.5)-y/(x2**2+y**2)**(1.5)
        velocidad+=(aceleracion*h)
        espacio+=(velocidad*h)
        if(abs(espacio[0])>xlim):break
        if(abs(espacio[1])>ylim):break
        if((x1**2+y**2)**0.5<=r):break
        if((x2**2+y**2)**0.5<=r):break
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
    return npa(pe)
def cuatro_cps(espacio,velocidad):
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    aceleracion = npa([0,0],dtype=np.float32)
    pt = np.arange(0,time,h)
    pe=[]
    pv=[]
    pa=[]
    for t in pt:
        x1=espacio[0]+d
        x2=espacio[0]-d
        x3=espacio[0]
        y=espacio[1]
        y2=y-b
        aceleracion[0]=-x1/(x1**2+y**2)**(1.5)-x2/(x2**2+y**2)**(1.5)-x3/(x3**2+y2**2)**(1.5)
        aceleracion[1]=-y/(x1**2+y**2)**(1.5)-y/(x2**2+y**2)**(1.5)-y2/(x3**2+y2**2)**(1.5)
        velocidad+=(aceleracion*h)
        espacio+=(velocidad*h)
        if(abs(espacio[0])>xlim):break
        if(abs(espacio[1])>ylim):break 
        if((x1**2+y**2)**0.5<=r):break
        if((x2**2+y**2)**0.5<=r):break
        if((x3**2+y2**2)**0.5<=r):break
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
    return npa(pe)
xlim=60
ylim=60
h=0.01
r=5
"""
time=1200
exercise="1.1"
espacio=[0,7]
plt.figure()
circle = plt.Circle((0, 0), r,lw=1,alpha=0.4)
plt.gca().add_artist(circle)
plt.gcf().suptitle(exercise+": x - y", fontsize=16)
plt.xlabel('espacio x')
plt.ylabel('espacio y')
plt.grid(True)
plt.gca().axis('equal')
for v in np.arange(0,1,0.05):
    pe=euler(espacio,[v,0])
    plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
plt.legend()
plt.savefig(exercise+" xy.png")
plt.show()    
"""
"""
r=2
time=1200
exercise="1.2"
espacio=[3,4]
plt.figure()
circle = plt.Circle((0, 0), r,lw=1,alpha=0.4)
plt.gca().add_artist(circle)
plt.gcf().suptitle(exercise+": x - y", fontsize=16)
plt.xlabel('espacio x')
plt.ylabel('espacio y')
plt.grid(True)
plt.gca().axis('equal')
for v in np.arange(0,1,0.05):
    pe=euler(espacio,[v,0])
    plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
plt.legend()
plt.savefig(exercise+" xy.png")
plt.show()
"""
"""
r=2
time=1200
exercise="1.2"
espacio=[3,4]
plt.figure()
circle = plt.Circle((0, 0), r,lw=1,alpha=0.4)
plt.gca().add_artist(circle)
plt.gcf().suptitle(exercise+": x - y", fontsize=16)
plt.xlabel('espacio x')
plt.ylabel('espacio y')
plt.grid(True)
plt.gca().axis('equal')
for v in np.arange(0,1,0.05):
    pe=euler(espacio,[v,0])
    plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
plt.legend()
plt.savefig(exercise+" xy.png")
plt.show()    
"""
"""
h=0.01
r=2
d=10
time=1000
exercise="2"
espacio=[10,10]
plt.figure()
pla1 = plt.Circle((-d, 0), r,lw=1,alpha=0.4)
pla2 = plt.Circle((d, 0), r,lw=1,alpha=0.4)
plt.gca().add_artist(pla1)
plt.gca().add_artist(pla2)
plt.gcf().suptitle(exercise+": x - y", fontsize=16)
plt.xlabel('espacio x')
plt.ylabel('espacio y')
plt.grid(True)
plt.gca().axis('equal')
for v in np.arange(0,1,0.1):
    pe=tres_cps(espacio,[v,0])
    plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
##v=0.3
##pe=tres_cps(espacio,[v,0])
##plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
plt.ylim((-ylim,ylim))
plt.xlim((-xlim,xlim))
plt.legend()
plt.savefig(exercise+" xy.png")
plt.show()
"""
"""
r=2
d=20
b=20
time=2000

espacio=[20,30]
exercise="desafio {},{}".format(espacio[0],espacio[1])
plt.figure()

pla1 = plt.Circle((-d, 0), r,lw=1,alpha=0.4)
pla2 = plt.Circle((d, 0), r,lw=1,alpha=0.4)
pla3 = plt.Circle((0, b), r,lw=1,alpha=0.4)
plt.gca().add_artist(pla1)
plt.gca().add_artist(pla2)
plt.gca().add_artist(pla3)
plt.gcf().suptitle(exercise+": x - y", fontsize=16)
plt.xlabel('espacio x')
plt.ylabel('espacio y')
plt.grid(True)
plt.gca().axis('equal')
for v in np.arange(0,1,0.1):
    pe=cuatro_cps(espacio,[v,0])
    plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
##v=0.3
##pe=cuatro_cps(espacio,[v,0])
##plt.plot(pe[:,0],pe[:,1],label="v={:.2}".format(v))
plt.ylim((-ylim,ylim))
plt.xlim((-xlim,xlim))
plt.legend()
plt.savefig(exercise+" xy.png")
plt.show()
"""
class Point():
    # Constructor de nuestra clase,el cual inicializara los valores por defecto de cada particula.
    def __init__(self,espacio,velocidad):
        self.velocidad=velocidad
        #mostramos en el plot los datos de cada particula 
        self.name="vx={:.1f}".format(velocidad[0])
        self.pe=cuatro_cps(espacio,velocidad)
    # Esta función dibujara las esfera y su rastro o desplazamiento que realiza.
    def draw(self,t):
        t=int(t)
        if(t<self.pe.shape[0]):
            plt.plot(self.pe[t][0],self.pe[t][1],'ro',alpha=0.5,label="vx={:.2}".format(self.velocidad[0]))
            plt.legend()
            if(t-l_line<=0):
                plt.plot(self.pe[:t,0],self.pe[:t,1])
            else:
                plt.plot(self.pe[t-l_line:t,0],self.pe[t-l_line:t,1])
r=2
d=20
b=20
ancho=60
largo=60
exercise ="animacion 4 cuerpos"
l_line=300
h=0.1
time=1200
pt = np.arange(0,time/h,50)
plt.xlim(-ancho, ancho) 
plt.ylim(-largo, largo)
points=None
pla1 = plt.Circle((-d, 0), r,lw=1,alpha=0.4)
pla2 = plt.Circle((d, 0), r,lw=1,alpha=0.4)
pla3 = plt.Circle((0, b), r,lw=1,alpha=0.4)
# Función que se llama en cada frame de la animación.
def init():
    global points
    points=[Point([20,30],[i,0]) for i in np.arange(0,1,0.1)]
#Funcion que se llama en cada iteracion,borrara y volvera a dibujar las particulas con su modificaciones
def chart(t):
    plt.gca().clear()
    plt.gca().add_patch(mp.Rectangle((-ancho, -largo), 2*ancho, 2*largo, fill=None,alpha=1,lw=2))
    plt.gca().add_artist(pla1)
    plt.gca().add_artist(pla2)
    plt.gca().add_artist(pla3)
    plt.gca().axis('equal')
    for point in points:
        point.draw(t)

# Creación y ejecución de la animación
ani= animation.FuncAnimation(plt.gcf(),chart,pt,init_func=init,interval=1)


try:
    plt.show()
except :
    print("TERMINO")
