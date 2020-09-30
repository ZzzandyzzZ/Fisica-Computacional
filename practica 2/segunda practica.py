from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from numpy import array as npa
import numpy as np
import matplotlib.animation as animation
import random as r
from mpl_toolkits.mplot3d import Axes3D

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
    plt.plot(pt,pa[:,0],label='aceleracion x')
    if(pa.shape[1]>=2):
        plt.plot(pt,pa[:,1],label='aceleracion y')
    if(pa.shape[1]==3):
        plt.plot(pt,pa[:,2],label='aceleracion z')
    plt.xlabel('tiempo')
    plt.ylabel('aceleracion')
    plt.title('a-t')
    plt.grid(True)
    plt.legend()
def plot_v_x():
    plt.subplot(2,2,4)
    plt.plot(pe[:,0],pv[:,0],label='velocidad x')
    if(pv.shape[1]>=2):
        plt.plot(pe[:,1],pv[:,1],label='velocidad y')
    if(pv.shape[1]==3):
        plt.plot(pe[:,2],pv[:,2],label='velocidad z')
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
    plt.savefig(name+" xy.png")
def plot_x_y_z(name):
    fig = plt.figure()
    plt.gcf().suptitle(name+": x - y - z", fontsize=16)
    ax = fig.gca(projection='3d')
    ax.plot(pe[:,0],pe[:,2],pe[:,1])
    plt.xlabel('espacio x')
    plt.ylabel('espacio z')
    ax.set_zlabel('espacio y')
    plt.grid(True)
    #plt.plot([pe[-1][0],espacio[0]],[pe[-1][2],espacio[2]],[pe[-1][1],espacio[1]])
    plt.savefig(name+" xyz.png")
def plot_v_x_t(name):
    fig = plt.figure()
    plt.gcf().suptitle(name+": v - x - t", fontsize=16)
    ax = fig.gca(projection='3d')
    ax.plot(pv[:,0],pe[:,0],pt)
    plt.xlabel('velocidad')
    plt.ylabel('espacio')
    ax.set_zlabel('tiempo')
    plt.grid(True)
    plt.savefig(name+".png")
def draw_all(name):
    plt.figure()
    plt.gcf().suptitle(name, fontsize=16)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plot_x_t()
    plot_v_t()
    plot_a_t()
    plot_v_x()
    plt.savefig(name+".png")
def euler(espacio,velocidad,aceleracion,inicio=True):
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    aceleracion = np.array(aceleracion,dtype=np.float32)
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
def euler_2(espacio,velocidad,aceleracion,inicio=True):
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    aceleracion = np.array(aceleracion,dtype=np.float32)
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

def euler_3(espacio,velocidad,aceleracion):
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    aceleracion = np.array(aceleracion,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    t=0
    while(True):
        t+=h
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        aceleracion[0]=-t*t/5
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        if(espacio[1]<0):break
    return npa(pe),npa(pv),npa(pa),t

def euler_4(espacio,velocidad,aceleracion):
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    aceleracion = np.array(aceleracion,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    t=0
    anterior=0
    while(True):
        t+=h
        anterior= espacio[1]
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        if(espacio[1]<anterior):break
    return npa(pe),npa(pv),npa(pa),t
h = 0.1
exercise ="1.1.1"
time=10
espacio=[0,-30]
velocidad = [0,-30]
aceleracion = [0,-10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#draw_all(exercise)

exercise ="1.1.2"
espacio=[0,0]
velocidad = [0,0]
aceleracion = [0,-10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#draw_all(exercise)


exercise ="1.1.3"
espacio=[0,30]
velocidad = [0,30]
aceleracion = [0,-10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#draw_all(exercise)

h = 0.05
exercise ="1.2.1"
time=20
espacio=[-30]
velocidad = [-30]
aceleracion = [10]
pt = np.arange(time,0,-h)
pe,pv,pa=euler(espacio,velocidad,aceleracion,False)
#draw_all(exercise)

exercise ="1.2.2"
espacio=[-30]
velocidad = [0]
aceleracion = [10]
pt = np.arange(time,0,-h)
pe,pv,pa=euler(espacio,velocidad,aceleracion,False)
#draw_all(exercise)

exercise ="1.2.3"
espacio=[30]
velocidad = [-30]
aceleracion = [10]
pt = np.arange(time,0,-h)
pe,pv,pa=euler(espacio,velocidad,aceleracion,False)
#draw_all(exercise)

exercise ="1.2.1 comprobacion"
espacio=[2570]
velocidad = [-230]
aceleracion = [10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#draw_all(exercise)

time =14
h=0.01
exercise ="1.3.1"
espacio=[0]
velocidad = [30]
aceleracion = [10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#plot_v_x_t(exercise)

exercise ="1.3.2"
espacio=[30]
velocidad = [0]
aceleracion = [10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#plot_v_x_t(exercise)

exercise ="1.3.3"
espacio=[0]
velocidad = [-30]
aceleracion = [10]
pt = np.arange(0,time,h)
pe,pv,pa=euler(espacio,velocidad,aceleracion)
#plot_v_x_t(exercise)
#draw_all(exercise)


h=0.01
exercise ="2.1"
espacio=[0,0]
velocidad = [2,3]
aceleracion = [0,-10]

pe,pv,pa,time=euler_3(espacio,velocidad,aceleracion)
pt = np.arange(0,time-h,h)
#draw_all(exercise)
#plot_x_y(exercise)

h=0.01
exercise ="2.2"
espacio=[-3,0,4]
velocidad = [2,3,4]
aceleracion = [0,-10,0]
pe,pv,pa,time=euler_3(espacio,velocidad,aceleracion)
pt = np.arange(0,time-h,h)
#draw_all(exercise)
#plot_x_y_z(exercise)

h=0.01

espacio=[0,3,0]
velocidad = [2,3,5]
aceleracion = [0,-10,0]
pe,pv,pa,time=euler_4(espacio,velocidad,aceleracion)
pt = np.arange(0,time-h,h)
#exercise ="2.3"
exercise ="2.3 time="+str(time)
#print("Tiempo: ",time)
#print("Coordenadas finales: ",pe[-1])
#print("Alcance vectorial: ",pe[-1]-espacio)

#draw_all(exercise)
#plot_x_y_z(exercise)

h=0.01
exercise ="3.1"
espacio=[10,10,10]
velocidad = [0,0,4]
aceleracion = [0,-10,0]
pe,pv,pa,time=euler_3(espacio,velocidad,aceleracion)
pt = np.arange(0,time-h,h)
#draw_all(exercise)
#plot_x_y_z(exercise)

class Point():
    # Constructor de nuestra clase,el cual inicializara los valores por defecto de cada particula.
    def __init__(self,espacio,velocidad,aceleracion):
        self.espacio=np.array(espacio,dtype=np.float32)
        self.velocidad = np.array(velocidad,dtype=np.float32)
        self.aceleracion = np.array(aceleracion,dtype=np.float32)
        self.name="ax={} ay={}".format(aceleracion[0],aceleracion[1])
        self.px=[]
        self.py=[]
    # Esta funcion actualizara la velocidad y espacio de la particula cada vez que sea invocada.
    def update(self,t):
        self.aceleracion[0]=-t*t/5

        self.espacio+=(self.velocidad*h)
        self.velocidad+=(self.aceleracion*h)
        self.px.append(self.espacio[0])
        self.py.append(self.espacio[1])
        # Esta condiciones hará que mantengamos un mismo tamaño del vector que guarda las velocidades, esto se vera como las colas de cada partícula.
        if(len(self.px)>l_line):
            self.px.pop(0)
            self.py.pop(0)
    # Esta función dibujara las esfera y su rastro o desplazamiento que realiza.
    def draw(self,t,line=True):
        self.update(t)
        plt.plot(self.espacio[0],self.espacio[1],'ro',alpha=0.5)
        if(line):plt.plot(self.px,self.py,label=self.name)
        plt.legend()

ancho=3
largo=0.3
exercise ="extra a=(variable,-10)"
# Tamaño del desplazamiento
l_line=10
h=0.01
time=0.41
pt = np.arange(0,time,h)
plt.xlim(0, ancho) 
plt.ylim(0, largo)
points=None
# Función que se llama en cada frame de la animación.
def init():
    global points
    points=[
            #Point([0,0],[5,2],[2,-10])
            Point([0,0],[30,30],[0,-10])
            #Point([0,0,0],[5,2,0],[2,-10,-1]),
            ]

def chart(t):
    plt.gca().clear()
    plt.gca().add_patch(mp.Rectangle((0, 0), ancho, largo, fill=None,alpha=1,lw=2))
    for point in points:
        point.draw(t)

# Creación y ejecución de la animación
ani= animation.FuncAnimation(plt.gcf(),chart,pt,init_func=init,interval=10,repeat_delay=400)


try:
    plt.show()
except :
    print("TERMINO")




h=0.001

espacio=[0,0]
velocidad = [50,50]
aceleracion = [0,-10]

pe,pv,pa,time=euler_3(espacio,velocidad,aceleracion)
print(time)
pt = np.arange(0,time-h,h)
#draw_all(exercise)
plot_x_y(exercise)
plt.show()
