import sys
sys.path.append('../')
from draw import *
def euler(espacio,velocidad,aceleracion):
    aceleracion = npa(aceleracion,dtype=np.float32)
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    pt = np.arange(0,time,h)
    pe=[]
    pv=[]
    pa=[]
    fc=[]
    for t in pt:
        aceleracion=(-a/r*espacio)
        #print(aceleracion)
        #print(np.sqrt(sum(aceleracion**2)))
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        #print(np.sqrt(sum(velocidad**2)))
        fuerza=m*np.sqrt(sum(aceleracion**2))
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        fc.append(fuerza.tolist())
    init(npa(pe),npa(pv),npa(pa),npa(fc),pt,[])
h=0.001
time=20
m=5
r=8
a=2

exercise="1.1 h=0.1"
aceleracion = [-a,0]
espacio=[r,0]
velocidad = [0,4]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)


exercise="1.2"
aceleracion = [0,-a]
espacio=[0,r]
velocidad = [-4,0]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)

exercise="1.3"
aceleracion = [a,0]
espacio=[-r,0]
velocidad = [0,-4]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)

exercise="1.4"
aceleracion = [0,a]
espacio=[0,-r]
velocidad = [4,0]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)

exercise="1.5"
aceleracion = [0,a]
espacio=[r*np.cos(np.pi/4),r*np.sin(np.pi/4)]
velocidad = [-4*np.cos(np.pi/4),4*np.sin(np.pi/4)]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)

exercise="1.7"
aceleracion = [0,a]
espacio=[r*np.cos(np.pi/4),r*np.sin(np.pi/4)]
velocidad = [-4*np.cos(np.pi/4),4*np.sin(np.pi/4)]
euler(espacio,velocidad,aceleracion)
##plot_x_y(exercise)
##draw_all(exercise)
##plot_f_t(exercise)
def euler_3(espacio,velocidad,aceleracion):
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    aceleracion = npa(aceleracion,dtype=np.float32)
    espacio_s=npa(espacio,dtype=np.float32)
    velocidad_s = npa(velocidad,dtype=np.float32)
    aceleracion_s = npa(aceleracion,dtype=np.float32)
    pe=[]
    pe_s=[]
    pv=[]
    pa=[]
    t=0
    while(True):
        t+=h
        v=mt.sqrt(sum(velocidad**2))
##        print(v)
##        print("A",aceleracion)
        aceleracion[0]=-k*v*velocidad[0]
        aceleracion[1]=-g-k*v*velocidad[1]
        
        if(espacio_s[1]>0):
            pe_s.append(espacio_s.tolist())
        if(espacio[1]<0):break
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        espacio_s+=(velocidad_s*h)
        velocidad_s+=(aceleracion_s*h)
        
    pt = np.arange(0,t,h)
    init(npa(pe),npa(pv),npa(pa),[],pt,npa(pe_s))
    
g=10
r=0.0367
C=0.5
A=np.pi*r**2
m=0.145
p=1.2
h=0.1
k=C*A*p/(2*m)
time=5
v=50
exercise="2"
aceleracion = [0,-10]
espacio=[0,0]
velocidad = [v*np.cos(np.pi/3),v*np.sin(np.pi/3)]
##euler_3(espacio,velocidad,aceleracion)
##plot_x_y(exercise,True)

#r=10 -100 namometros 
#r = 100 - 160 namometros 
#m = 50 -2000 aminoacidos
#m = 5500 220000 masa
g=10
r=0.005
##r=0.0005
vol=4/3*np.pi*r**3
C=0.5
A=np.pi*r**2
d=1000
m=d*vol
print(m)
p=1.2
h=0.01
k=C*A*p/(2*m)
time=5
exercise="desafio"
aceleracion = [0,-10]
espacio=[0,16]
velocidad = [16,0]
##euler_3(espacio,velocidad,aceleracion)
##plot_x_y(exercise,True)

def euler_3(espacio,velocidad,aceleracion,h):
    aceleracion = npa(aceleracion,dtype=np.float32)
    espacio=npa(espacio,dtype=np.float32)
    velocidad = npa(velocidad,dtype=np.float32)
    pt = np.arange(0,time,h)
    error=[]
    for t in pt:
        aceleracion=(-a/r*espacio)
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        er=abs(r-np.sqrt(sum(espacio**2)))
        error.append(er)
    return error,pt
def plot_error(h):
    print(h)
    plt.gcf().suptitle(exercise+": e - t", fontsize=16)
    plt.plot(pt,error,label="h={} %er={}".format(h,np.mean(error)/r*100))
    plt.xlabel('tiempo')
    plt.ylabel('error')
    plt.grid(True)
    plt.legend()
    
h=0.01
time=15
a=2
r=8
exercise="4"
aceleracion = [-a,0]
espacio=[r,0]
velocidad = [0,4]
plt.figure()
for i in range(1,5):   
    error,pt=euler_3(espacio,velocidad,aceleracion,1/(10**i))
    plot_error(1/10**i)
plt.savefig(exercise+" error.png")
print(np.mean(error)/r*100)
euler(espacio,velocidad,aceleracion)

plot_x_y(exercise)
plt.show()


#plot_x_y(exercise)
#draw_all(exercise)
