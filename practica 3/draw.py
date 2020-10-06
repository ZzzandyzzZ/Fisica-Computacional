from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from numpy import array as npa
import numpy as np
import matplotlib.animation as animation
import random as r
from mpl_toolkits.mplot3d import Axes3D
import math as mt
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
def plot_x_y(name,simultaneo=False):
    plt.figure()
    plt.gcf().suptitle(name+": x - y", fontsize=16)
    if(simultaneo):
        plt.plot(pe[:,0],pe[:,1],label='con fuerza arrastre')
        plt.plot(pe_s[:,0],pe_s[:,1],label='sin fuerza arrastre')
        plt.legend()
    else:
        plt.plot(pe[:,0],pe[:,1])
    plt.plot(pe[0,0],pe[0,1],'ro',alpha=0.5)
    plt.xlabel('espacio x')
    plt.ylabel('espacio y')
    plt.grid(True)
    plt.gca().axis('equal')
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

def plot_f_t(name):
    plt.figure()
    plt.gcf().suptitle(name+": f - t", fontsize=16)
    plt.plot(pt,fc)
    plt.xlabel('tiempo')
    plt.ylabel('fuerza')
    plt.grid(True)
    plt.savefig(name+" xy.png")

def draw_all(name):
    plt.figure()
    plt.gcf().suptitle(name, fontsize=16)
    plt.subplots_adjust(wspace=0.5, hspace=0.5)
    plot_x_t()
    plot_v_t()
    plot_a_t()
    plot_v_x()
    plt.savefig(name+".png")
def init(Pe,Pv,Pa,Fc,Pt,Pe_s):
    global pe,pv,pa,fc,pt,pe_s
    pe=Pe
    pv=Pv
    pa=Pa
    fc=Fc
    pt=Pt
    pe_s =Pe_s
pe,pv,pa,fc,pt,pe_s = [],[],[],[],[],[]
