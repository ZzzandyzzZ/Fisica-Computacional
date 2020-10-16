import sys
sys.path.append('../')
from draw import *

def euler(espacio,velocidad,aceleracion):
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    vU=[]
    vK=[]
    vE=[]
    for t in pt:
        aceleracion=-k*espacio/m-c*velocidad/m+f0*np.cos(w*t_)/m
        espacio+=(velocidad*h)
        velocidad+=(aceleracion*h)
        U=1/2*k*espacio**2
        K=1/2*m*velocidad**2
        E=U+K
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        vU.append(U)
        vK.append(K)
        vE.append(E)
    init(npa(pe),npa(pv),npa(pa),[],pt,[],vU,vK,vE)
def punto_medio(espacio,velocidad):
    global t
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    vU=[]
    vK=[]
    vE=[]
    aceleracion=-k*espacio/m-c*velocidad/m+f0*np.cos(w*t)/m
    velocidad+=aceleracion*h/2
    for t in pt:
        aceleracion=-k*espacio/m-c*velocidad/m+f0*np.cos(w*t)/m 
        velocidad+=(aceleracion*h)
        espacio+=(velocidad*h)
        U=1/2*k*espacio**2
        K=1/2*m*velocidad**2
        E=U+K
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        vU.append(U)
        vK.append(K)
        vE.append(E)
    init(npa(pe),npa(pv),npa(pa),[],pt,[],vU,vK,vE)
h = 0.001
k=0.1
m=0.2
f0=0
c=0
w=0
exercise ="1.1"
time=40
t=0
espacio=[2]
velocidad = [0]
aceleracion=[0]
pt = np.arange(0,time,h)
##punto_medio(espacio,velocidad)
##draw_all(exercise+" punto medio")
##draw_all2(exercise+"energia")
##euler(espacio,velocidad,aceleracion)
##draw_all(exercise+" euler")
##draw_all2(exercise+"energia")
##together(exercise)
exercise ="1.2"
k=0.1
m=0.2
c=0.05
f0=0
w=0
espacio=[0]
velocidad = [-2]
aceleracion=[0]
pt = np.arange(0,time,h)
##punto_medio(espacio,velocidad)
##draw_all(exercise+" punto medio")
##plot_v_x_t(exercise)
time=120
exercise ="1.3"
k=0.1
m=0.2
c=0.05
f0=0.01
w=0.3
espacio=[-1]
velocidad = [1]
aceleracion=[0]
pt = np.arange(0,time,h)
##punto_medio(espacio,velocidad)
##draw_all(exercise+" punto medio")
##plot_v_x_t(exercise)
def punto_medio2(espacio,velocidad):
    global t
    espacio=np.array(espacio,dtype=np.float32)
    velocidad = np.array(velocidad,dtype=np.float32)
    espacio2=np.array(espacio,dtype=np.float32)
    velocidad2 = np.array(velocidad,dtype=np.float32)
    pe=[]
    pv=[]
    pa=[]
    pe2=[]
    pv2=[]
    pa2=[]
    aceleracion=-k*espacio/m-c*velocidad/m+f0*np.cos(w*t)/m
    velocidad+=aceleracion*h/2
    for t in pt:
        aceleracion=-k*espacio/m-c*velocidad/m+f0*np.cos(w*t)/m 
        velocidad+=(aceleracion*h)
        espacio+=(velocidad*h)
        pe.append(espacio.tolist())
        pv.append(velocidad.tolist())
        pa.append(aceleracion.tolist())
        aceleracion2=-k*espacio2/m-c*velocidad2/m
        velocidad2+=(aceleracion2*h)
        espacio2+=(velocidad2*h)
        pe2.append(espacio2.tolist())
        pv2.append(velocidad2.tolist())
        pa2.append(aceleracion2.tolist())
    return npa(pe),npa(pv),npa(pa),npa(pe2),npa(pv2),npa(pa2)
time=100
exercise ="desafio"
k=0.1
m=0.2
c=0.05
f0=0.01
w=0.3
espacio=[-1]
velocidad = [1]
aceleracion=[0]
pt = np.arange(0,time,h)
pe,pv,pa,pe2,pv2,pa2=punto_medio2(espacio,velocidad)

plt.figure()
plt.gcf().suptitle(exercise, fontsize=16)
plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.subplot(2,2,1)
plt.plot(pt,pe[:,0],pt,pe2[:,0])
plt.xlabel('tiempo')
plt.ylabel('espacio')
plt.title('X-T')
plt.grid(True)
plt.subplot(2,2,2)
plt.plot(pt,pv[:,0],pt,pv2[:,0])
plt.xlabel('tiempo')
plt.ylabel('velocidad')
plt.title('V-T')
plt.grid(True)
plt.subplot(2,2,3)
plt.plot(pt,pa[:,0],pt,pa2[:,0])
plt.xlabel('tiempo')
plt.ylabel('aceleración')
plt.title('A-T')
plt.grid(True)
plt.subplot(2,2,4)
plt.plot(pe[:,0],pv[:,0],pe2[:,0],pv2[:,0])
plt.xlabel('velocidad')
plt.ylabel('espacio')
plt.title('espacio de fases')
plt.grid(True)
plt.savefig(exercise+".png")
fig = plt.figure()
plt.gcf().suptitle(exercise+": v - x - t", fontsize=16)
ax = fig.gca(projection='3d')
ax.plot(pv[:,0],pe[:,0],pt)
ax.plot(pv2[:,0],pe2[:,0],pt)
plt.xlabel('velocidad')
plt.ylabel('espacio')
ax.set_zlabel('tiempo')
plt.grid(True)
plt.savefig(exercise+"3d.png")


plt.show()
