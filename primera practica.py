"""
#DESAFIO SIMPLE

import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
import matplotlib.animation as animation

fig = plt.figure()
axs = fig.gca()
largo=20
ancho=10
l_line=20
rect1 = mp.Rectangle((0, 0), ancho, largo, fill=None,alpha=1,lw=2)
h=0.1
x=5
y=15
vx=2
vy=3
ax=0
ay=0
px=[]
py=[]
pt = np.arange(0,5,h)
plt.xlim([-5, 15]) 
plt.ylim([-5, 25])
 
def mov(t):
    global x,y,vx,vy,largo,ancho
    if(y>largo-0.3 or y<0+0.3):vy*=-1
    if(x>ancho-0.1 or x<0+0.1):vx*=-1
    x+=vx*h
    y+=vy*h
    vx+=ax*h
    vy+=ay*h
    px.append(x)
    py.append(y)
    axs.clear()
    axs.add_patch(rect1)
    plt.plot(x,y,'ro',alpha=0.5)
    if(len(px)>l_line):
        px.pop(0)
        py.pop(0)
    plt.plot(px,py)

ani= animation.FuncAnimation(fig,mov,pt,interval=1)
try:
    plt.show()
except:
    print("FINALIZO")

"""
#DESAFIO MULTIPLE
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from numpy import array as npa
import numpy as np
import matplotlib.animation as animation
import random as r
from mpl_toolkits.mplot3d import Axes3D

class Point():
    # Constructor de nuestra clase,el cual inicializara los valores por defecto de cada particula.
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.px=[]
        self.py=[]
    # Esta funcion actualizara la velocidad y espacio de la particula cada vez que sea invocada.
    def update(self):
        # Estas condiciones son las que invertirán la dirección de la partícula, cada vez que llegue a un borde.
        if(self.y>=largo or self.y<=0):self.vy*=-1
        if(self.x>=ancho or self.x<=0):self.vx*=-1
        self.x+=self.vx*h
        self.y+=self.vy*h
        self.px.append(self.x)
        self.py.append(self.y)
        # Esta condiciones hará que mantengamos un mismo tamaño del vector que guarda las velocidades, esto se vera como las colas de cada partícula.
        if(len(self.px)>l_line):
            self.px.pop(0)
            self.py.pop(0)
    # Esta función dibujara las esfera y su rastro o desplazamiento que realiza.
    def draw(self,line=True):
        self.update()
        plt.plot(self.x,self.y,'ro',alpha=0.5)
        if(line):plt.plot(self.px,self.py)
# Largo y ancho del rectangulo
largo=20
ancho=10
# Numero de partículas
n=10
# Rango de velocidades
rn=10
# Tamaño del desplazamiento
l_line=5
h=0.01
pt = np.arange(0,5,h)
plt.xlim([-5, ancho+5]) 
plt.ylim([-5, largo+5])
points=[]
# Inicializamos un vector con velocidades aleatorias
for i in range(n):
    points.append(Point(ancho/2,largo/2,r.randrange(-rn,rn),r.randrange(-rn,rn)))
# Función que se llama en cada frame de la animación.
def chart(t):
    plt.gca().clear()
    plt.gca().add_patch(mp.Rectangle((0, 0), ancho, largo, fill=None,alpha=1,lw=2))
    for p in points:
        p.draw()
# Creación y ejecución de la animación
ani= animation.FuncAnimation(plt.gcf(),chart,pt,interval=10)

try:
    plt.show()
except:
    print("FINALIZO")


def plot_x_t():
    plt.subplot(2,2,1)
    plt.plot(pt,pe[:,0],label='espacio x')
    if(pv.shape[1]>=2):
        plt.plot(pt,pe[:,1],label='espacio y')
    if(pv.shape[1]==3):
        plt.plot(pt,pe[:,2],label='espacio z')
    plt.xlabel('tiempo')
    plt.ylabel('espacio')
    plt.title('x-t')
    plt.grid(True)
    plt.legend()
def plot_v_t():
    plt.subplot(2,2,2)
    plt.plot(pt,pv[:,0],label='velocidad x')
    if(pv.shape[1]>=2):
        plt.plot(pt,pv[:,1],label='velocidad y')
    if(pv.shape[1]==3):
        plt.plot(pt,pv[:,2],label='velocidad z')
    plt.xlabel('tiempo')
    plt.ylabel('velocidad')
    plt.title('v-t')
    plt.grid(True)
    plt.legend()
def plot_a_t():
    plt.subplot(2,2,3)
    plt.plot(pt,pa)
    plt.xlabel('tiempo')
    plt.ylabel('aceleracion')
    plt.title('a-t')
    plt.grid(True)
def plot_v_x():
    plt.subplot(2,2,4)
    plt.plot(pe[:,0],pv[:,0],label='velocidad x')
    if(pv.shape[1]>=2):
        plt.plot(pe[:,0],pv[:,1],label='velocidad y')
    if(pv.shape[1]==3):
        plt.plot(pt,pv[:,2],label='velocidad z')
    plt.xlabel('espacio')
    plt.ylabel('velocidad')
    plt.title('espacio de fases')
    plt.grid(True)
    plt.legend()
def plot_x_y(name):
    plt.figure()
    plt.gcf().suptitle(name+": x - y", fontsize=16)
    plt.plot(pe[:,0],pe[:,1])
    plt.xlabel('espacio x')
    plt.ylabel('espacio y')
    plt.grid(True)
def plot_x_y_z(name):
    fig = plt.figure()
    plt.gcf().suptitle(name+": x - y - z", fontsize=16)
    ax = fig.gca(projection='3d')
    ax.plot(pe[:,0],pe[:,1],pe[:,1])
    plt.xlabel('espacio x')
    plt.ylabel('espacio y')
    ax.set_zlabel('espacio z')
    plt.grid(True)
def plot_v_x_t():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(pv[:,0],pe[:,0],pt)
    plt.xlabel('velocidad')
    plt.ylabel('espacio')
    plt.grid(True)
def draw_all(name):
    plt.figure()
    plt.gcf().suptitle(name, fontsize=16)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plot_x_t()
    plot_v_t()
    plot_a_t()
    plot_v_x()
    
def euler_(espacio,velocidad,aceleracion,inicio=True):    
    px=[]
    py=[]
    pvx=[]
    pvy=[]
    pa=[]
    t=0
    for t in pt:
        espacio+=velocidad*h*a
        velocidad+=aceleracion*h*a
        px.append(espacio[0])
        py.append(espacio[1])
        pvx.append(velocidad[0])
        pvy.append(velocidad[1])
        pa.append(aceleracion)
    return px,py,[pvx,pvy],pa

def euler(espacio,velocidad,aceleracion,inicio=True):    
    pe=[]
    pv=[]
    pa=[]
    a =1 if inicio else -1
    for t in pt:
        espacio+=(velocidad*h*a)
        velocidad+=(aceleracion*h*a)
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
    return npa(pe),npa(pv),npa(pa)
def euler2(espacio,velocidad,aceleracion):
    pe=[]
    pv=[]
    pa=[]
    for t in pt:
        if(t==3):velocidad+=3
        if(t==8):velocidad=3
        if(t==10):velocidad+=-5
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
    return npa(pe),npa(pv),npa(pa)

def euler3(distancia,aceleracion):
    i=0
    espacio=npa([0])
    while(espacio!=distancia):
        i+=0.5
        espacio=npa([0],dtype=np.float32)
        velocidad=npa([i],dtype=np.float32)
        pe=[]
        pv=[]
        pa=[]
        for t in pt:
            espacio+=(velocidad*h)
            velocidad+=(aceleracion*h)
            pe.append(espacio.tolist())
            pv.append(velocidad.tolist())
            pa.append(aceleracion)
    return npa(pe),npa(pv),npa(pa)
"""
h=0.01
time=10
pt = np.arange(0,time,h)
exercise="1.1.1"
espacio=np.array([-5],dtype=np.float32)
velocidad = np.array([2],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")

time=10
pt = np.arange(0,time,h)
exercise="1.1.2"
espacio=np.array([7],dtype=np.float32)
velocidad = np.array([-2],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")

time=10
pt = np.arange(0,time,h)
exercise="1.1.3"
espacio=np.array([-5],dtype=np.float32)
velocidad = np.array([3],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler2(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")

time=10
pt = np.arange(time,0,-h)
exercise="1.1.4"
espacio=np.array([2],dtype=np.float32)
velocidad = np.array([4],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion,False)
draw_all(exercise)
plt.savefig(exercise+".png")
print(espacio[-1])

time=10
pt = np.arange(0,time,h)
exercise="1.1.4"
espacio=np.array([-38],dtype=np.float32)
velocidad = np.array([4],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise+"_cmp")
plt.savefig(exercise+"_cmp.png")
print(espacio[-1])

time=2
pt = np.arange(0,time,h)
exercise="1.1.5"
distancia=300
pe,pv,pa=euler3(distancia,0)
draw_all(exercise)
plt.savefig(exercise+".png")
print(espacio[-1])


time=5
pt = np.arange(0,time,h)
exercise ="1.2.1"
espacio=np.array([3,4],dtype=np.float32)
velocidad = np.array([-2,0],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")
plot_x_y(exercise)
plt.savefig(exercise+" x - y.png")

time=5
pt = np.arange(0,time,h)
exercise ="1.2.2"
espacio=np.array([-3,-4],dtype=np.float32)
velocidad = np.array([2,4],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")
plot_x_y(exercise)
plt.savefig(exercise+" x - y.png")

time=10
pt = np.arange(0,time,h)
exercise ="1.2.3"
espacio=np.array([4,-3],dtype=np.float32)
velocidad = np.array([1,2],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")
plot_x_y(exercise)
plt.savefig(exercise+" x - y.png")

time=5
pt = np.arange(time,0,-h)
exercise ="1.3.1"
espacio=np.array([-3,-4,-5],dtype=np.float32)
velocidad = np.array([0,2,4],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion,False)
draw_all(exercise)
plt.savefig(exercise+".png")
plot_x_y_z(exercise)
plt.savefig(exercise+" x - y - z.png")

time=10
pt = np.arange(0,time,h)
exercise ="1.3.2"
espacio=np.array([3,-4,5],dtype=np.float32)
velocidad = np.array([-2,1,11],dtype=np.float32)
aceleracion = np.array([0],dtype=np.float32)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
draw_all(exercise)
plt.savefig(exercise+".png")
plot_x_y_z(exercise)
plt.savefig(exercise+" x - y - z.png")
"""
plt.show()
