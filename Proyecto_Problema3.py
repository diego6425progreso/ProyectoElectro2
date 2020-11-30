#Programa para correr problema 3.3 de proyecto
#Diego Contreras/Ruben Lima/Diego de Leon
import numpy as np
from scipy import signal as sp
import matplotlib.pylab as plt
from sympy import *
import math
#ademas importamos las variables simbolicas 'n' y 't'
#from sympy.abc import t
tec=[]
tes=[]
tet=[]
tec.append([0,0,0,0,0,0,0,0,0,0,0])
tes.append([0,0,0,0,0,0,0,0,0,0,0])
tet.append([0,0,0,0,0,0,0,0,0,0,0])
tmc=[]
tms=[]
tmt=[]
tmc.append([0,0,0,0,0,0,0,0,0,0,0])
tms.append([0,0,0,0,0,0,0,0,0,0,0])
tmt.append([0,0,0,0,0,0,0,0,0,0,0])
bc=[0];
ac=[0];
bs=[0];
#at=[0];
bt=[0];
at=[0];
fc=[0];
fs=[0];
ft=[0];
#print(tec)

def grafcomp(onda,modo,T):
    #onda: 0=cuadrada, 1=sierra, 2=triangular   modo: 0=te 1=tm
    x =np.linspace(0,T*4, 30)
    z=0
    armonicos=10
    yc=0
    ys=0
    yt=0
    global bc
    global bs
    global at
    for n in range(1,armonicos+1):
        yc=yc+bc[n]*np.sin((np.pi*n*2*t)/T)
    for n in range(1,armonicos+1):
        ys=ys+bs[n]*np.sin((np.pi*n*t)/T)
    for n in range(1,armonicos+1):  
        yt=yt+at[n]*np.cos((np.pi*((2*n)-1)*t)/T)
    if(onda==0):
        y=yc
        if (modo==0):
            for n in range(1,armonicos+1):
                Ex=bc[n]
                zeta=1
                cpro=tec[n][2]
                atenuacion=math.exp(-zeta*tec[n][2])
                if(tec[n][6]==True):#coseno
                    z = z+ bc[n]*np.sin((np.pi*n*2*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+ bc[n]*np.sin((np.pi*n*2*t)/T)*atenuacion
        if (modo==1):
            for n in range(1,armonicos+1):
                Ex=bc[n]
                zeta=1
                cpro=tmc[n][2]
                atenuacion=math.exp(-zeta*tmc[n][2])
                if(tmc[n][6]==True):#coseno
                    z = z+ bc[n]*np.sin((np.pi*n*2*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+ bc[n]*np.sin((np.pi*n*2*t)/T)*atenuacion                    

    if(onda==1):
        y=ys
        if (modo==0):
            for n in range(1,armonicos+1):
                Ex=bs[n]
                zeta=1
                cpro=tes[n][2]
                atenuacion=math.exp(-zeta*tes[n][2])
                if(tes[n][6]==True):#coseno
                    z = z+ bs[n]*np.sin((np.pi*n*2*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+ bs[n]*np.sin((np.pi*n*2*t)/T)*atenuacion
        if (modo==1):
            for n in range(1,armonicos+1):
                Ex=bs[n]
                zeta=1
                cpro=tms[n][2]
                atenuacion=math.exp(-zeta*tms[n][2])
                if(tms[n][6]==True):#coseno
                    z = z+ bs[n]*np.sin((np.pi*n*2*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+ bs[n]*np.sin((np.pi*n*2*t)/T)*atenuacion


    if(onda==2):
        y=yt
        if (modo==0):
            for n in range(1,armonicos+1):
                Ex=at[n]
                zeta=1
                cpro=tet[n][2]
                atenuacion=math.exp(-zeta*tet[n][2])
                if(tet[n][6]==True):#coseno
                    z = z+ at[n]*np.cos((np.pi*((2*n)-1)*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+ at[n]*np.cos((np.pi*((2*n)-1)*t)/T)*atenuacion
        if (modo==1):
            for n in range(1,armonicos+1):
                Ex=at[n]
                zeta=1
                cpro=tmt[n][2]
                atenuacion=math.exp(-zeta*tmt[n][2])
                if(tms[n][6]==True):#coseno
                    z = z+ at[n]*np.cos((np.pi*((2*n)-1)*t)/T)*np.cos(-cpro*zeta)
                else:
                    z = z+at[n]*np.cos((np.pi*((2*n)-1)*t)/T)*atenuacion
    fig, ax = plt.subplots(2)
    ax[0].plot(x, y)
    ax[1].plot(x,z)
    plt.show()
    #ax.set_title('A single plot')
    
def graficartran(onda,modo,campo):
    #onda: 0=cuadrada, 1=sierra, 2=triangular   modo: 0=te 1=tm
    #campo: 0=ex 1=ey 2=hx 3=hy
    m=1
    n=0
    z=0
    global tec
    global tes
    global tet
    global tmc
    global tms
    global tmt
    global bc
    global bs
    global at
    if(onda==0):
        for x in range(1,11):
            if(modo==0):
                a=tec[x][0]
                b=tec[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tec[x][9]
                ey=tec[x][10]
                hx=tec[x][7]
                hy=tec[x][8]
                cpro=tec[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tec[x][2])
            else:
                a=tmc[x][0]
                b=tmc[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tmc[x][9]
                ey=tmc[x][10]
                hx=tmc[x][7]
                hy=tmc[x][8]
                cpro=tmc[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tmc[x][2])
            if(campo==0):
                z = z+ex*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==1):
                z =z+ ey*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==2):
                z = z+hx*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            else:
                z =z+ hy*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)



    if(onda==1):
        for x in range(1,11):
            if(modo==0):
                a=tes[x][0]
                b=tes[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tes[x][9]
                ey=tes[x][10]
                hx=tes[x][7]
                hy=tes[x][8]
                cpro=tes[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tes[x][2])
            else:
                a=tms[x][0]
                b=tms[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tms[x][9]
                ey=tms[x][10]
                hx=tms[x][7]
                hy=tms[x][8]
                cpro=tms[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tms[x][2])
            if(campo==0):
                z = z+ex*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==1):
                z =z+ ey*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==2):
                z = z+hx*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            else:
                z =z+ hy*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)

    if(onda==2):
        for x in range(1,11):
            if(modo==0):
                a=tet[x][0]
                b=tet[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tet[x][9]
                ey=tet[x][10]
                hx=tet[x][7]
                hy=tet[x][8]
                cpro=tet[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tet[x][2])
            else:
                a=tmt[x][0]
                b=tmt[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                ex=tmt[x][9]
                ey=tmt[x][10]
                hx=tmt[x][7]
                hy=tmt[x][8]
                cpro=tmt[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tmt[x][2])
            if(campo==0):
                z = z+ex*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==1):
                z =z+ ey*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            elif(campo==2):
                z = z+hx*np.sin((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
            else:
                z =z+ hy*np.cos((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)


    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')


    # Plot a 3D surface
    #ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
    #ax.contour3D(x, y, z, 50, cmap='binary')
    ax.plot_wireframe(x1, y1, z, color='black')
    #ax.plot_wireframe(x, y, z1, color='black')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
    
def graficarlon(onda,modo):
    #onda: 0=cuadrada, 1=sierra, 2=triangular   modo: 0=te 1=tm
    global tec
    global tes
    global tet
    global tmc
    global tms
    global tmt
    global bc
    global bs
    global at
    #x = np.outer(np.linspace(0,a, 30), np.ones(30))
    #y = x.copy().T # transpose
    #y = (np.outer(np.linspace(0,b,30),np.ones(30))).T
    m=1
    n=0
    z=0
    if(onda==0):
        for x in range(1,11):
            if(modo==0):
                a=tec[x][0]
                b=tec[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=bc[x]
                cpro=tec[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tec[x][2])
                if(tec[x][6]==True):
                    z = z+Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)    
                else:
                    z = z+ Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*atenuacion

            if(modo==1):
                a=tmc[x][0]
                b=tmc[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=bc[x]
                cpro=tmc[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tmc[x][2])
                if(tmc[x][6]==True):
                    z = z+ Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
                else:
                    z = z+Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*atenuacion

    if(onda==1):
        for x in range(1,11):
            if(modo==0):
                a=tes[x][0]
                b=tes[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=bs[x]
                cpro=tes[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tes[x][2])
                if(tes[x][6]==True):
                    z = z+Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)    
                else:
                    z = z+ Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*atenuacion

            if(modo==1):
                a=tms[x][0]
                b=tms[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=bs[x]
                cpro=tms[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tms[x][2])
                if(tms[x][6]==True):
                    z = z+ Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
                else:
                    z = z+Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*atenuacion


    if(onda==2):
        for x in range(1,11):
            if(modo==0):
                a=tet[x][0]
                b=tet[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=at[x]
                cpro=tet[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tet[x][2])
                if(tes[x][6]==True):
                    z = z+Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*np.cos(-cpro*zeta)    
                else:
                    z = z+ Ex*np.cos((math.pi*x1*m)/a)*np.cos((math.pi*y1*n)/b)*atenuacion

            if(modo==1):
                a=tmt[x][0]
                b=tmt[x][1]
                x1 = np.outer(np.linspace(0,a, 30), np.ones(30))
                #y = x.copy().T # transpose
                y1 = (np.outer(np.linspace(0,b,30),np.ones(30))).T
                Ex=at[x]
                cpro=tmt[x][2]
                zeta=1
                atenuacion=math.exp(-zeta*tmt[x][2])
                if(tms[x][6]==True):
                    z = z+ Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*np.cos(-cpro*zeta)
                else:
                    z = z+Ex*np.sin((math.pi*x1*m)/a)*np.sin((math.pi*y1*n)/b)*atenuacion

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')


    # Plot a 3D surface
    #ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
    #ax.contour3D(x, y, z, 50, cmap='binary')
    ax.plot_wireframe(x1, y1, z, color='black')
    #ax.plot_wireframe(x, y, z1, color='black')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
                
            
def te10(f,ez,tipo):
    global tec
    global tes
    global tet
    global bc
    global bs
    global at
    fc=16.0
    #print("Frecuencia de corte elegida: "+str(fc/1e9))
    #f=f*1e9
    w=2*math.pi*f
    fc=fc*1e9
    e=8.8541e-12
    u=1.2566e-8
    m=1
    n=0
    c=3e8
    a=0
    b=1
    beta=0
    cpro=0
    ntm=0
    nte=0
    ez=20
    cpc=False
    if(f>fc):
        beta=1
        cpro=((w)/c)*((1-((fc/f)**2))**0.5)
        nte=(w*u)/(cpro)
        vel=w/cpro
        long=(2*math.pi)/cpro
        vel=round(vel,2)
        long=round(long,5)
        cpc=True
    elif f==fc:
        cpro=0
        ntm=0
        nte=0
        vel="no aplica"
        long="no aplica"
        cpc=False
    else:
        cpro=(w/c)*((((fc/f)**2)-1)**0.5)
        ntm=(cpro)/(w*e*1j)
        nte=(1j*w*u)/cpro
        vel="no aplica"
        long="no aplica"
        cpc=False
    cpro1=cpro*1j
    kc=cpro1**2+(w**2)*u*e


    cpro=round(cpro,2)
    try:
        nte=round(nte,2)
        ntm= round(ntm,2)
    except:
        nte=nte
    a=float((((float(m)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(n)*math.pi)/float(b))**2)))**0.5)
    a=round(a,5)
    ex=((1j*w*u*n*math.pi)/(kc*b))*ez
    ey=((-1j*w*u*m*math.pi)/(kc*a))*ez
    hx=((cpro1*m*math.pi)/(kc*a))*ez    
    hy=((cpro1*n*math.pi)/(kc*b))*ez
    ex=abs(ex)
    ey=abs(ey)
    hx=abs(hx)
    hy=abs(hy)
    if(tipo==0):
        tec.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])
    if(tipo==1):
        tes.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])
    if(tipo==2):
        tet.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])

def tm10(f,ez,tipo):
    global tmc
    global tms
    global tmt
    fc=16.0
    #print("Frecuencia de corte elegida: "+str(fc/1e9))
    #f=f*1e9
    w=2*math.pi*f
    fc=fc*1e9
    e=8.8541e-12
    u=1.2566e-8
    m=1
    n=0
    c=3e8
    a=0
    b=1
    beta=0
    cpro=0
    ntm=0
    nte=0
    ez=20
    cpc=False
    if(f>fc):
        beta=1
        cpro=((w)/c)*((1-((fc/f)**2))**0.5)
        ntm=(cpro)/(w*e)
        nte=(w*u)/(cpro)
        vel=w/cpro
        long=(2*math.pi)/cpro
        vel=round(vel,2)
        long=round(long,5)
        cpc=True
    elif f==fc:
        cpro=0
        ntm=0
        nte=0
        vel="no aplica"
        long="no aplica"
        cpc=False
    else:
        cpro=(w/c)*((((fc/f)**2)-1)**0.5)
        ntm=(cpro)/(w*e*1j)
        nte=(1j*w*u)/cpro
        vel="no aplica"
        long="no aplica"
        cpc=False
    cpro1=cpro*1j
    kc=cpro1**2+(w**2)*u*e


    cpro=round(cpro,2)
    try:
        nte=round(nte,2)
        ntm= round(ntm,2)
    except:
        nte=nte
    a=(c**2)/4*(fc**2)
    #b=float((((float(n)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(m)*math.pi)/float(a))**2)))**0.5)
    #b=round(b,5)
    b=1
    #print(b)
    ex=((cpro1*m*math.pi)/(kc*a))*ez
    ey=((cpro1*n*math.pi)/(kc*b))*ez
    hx=((w*e*-1j*n*math.pi)/(kc*b))*ez
    hy=((w*e*-1j*m*math.pi)/(kc*a))*ez
    ex=abs(ex)
    ey=abs(ey)
    hx=abs(hx)
    hy=abs(hy)
    if(tipo==0):
        tmc.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])
    if(tipo==1):
        tms.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])
    if(tipo==2):
        tmt.append([a,b,cpro,nte,vel,long,cpc,hx,hy,ex,ey])

A=5
f=20e9
T=1/f
t=np.linspace(0,T*4, 30)
armonicos=1000      
serie=0
print("")
#Señal cuadrada
for n in range(1,armonicos+1):
    bc.append((2*A-2*A*cos(n*np.pi))/(n*np.pi))
#print (b)    
yc=0
for n in range(1,armonicos+1):
    yc=yc+bc[n]*np.sin((np.pi*n*2*t)/T)
    fc.append(((np.pi*n*2)/T)/(2*np.pi))
print("Armonicos para onda cuadrada con frecuencia: "+str(f)+"Hz")    
for x in range (1,11):
    print(str(x)+" Armonico, b["+str(x)+"]= "+str(bc[x])+" y frecuencia:"+str(fc[x]))
    print("Solucion en TE10")
    te10(fc[x],bc[x],0)
    print(" Constante de propagación: "+str(tec[x][2]))
    print(" Impedancia: "+str(tec[x][3]))
    print(" Velocidad: "+str(tec[x][4]))
    print("Soluciones TM10")
    tm10(fc[x],bc[x],0)
    print(" Constante de propagación: "+str(tmc[x][2]))
    print(" Impedancia: "+str(tmc[x][3]))
    print(" Velocidad: "+str(tmc[x][4]))
    print("")

print("Características de la guia de onda, TE10, frecuencia de corte=16Ghz  a="+str(tec[2][0])+", b= indiferente")
print("Características de la guia de onda, TM10, frecuencia de corte=16Ghz  a="+str(tmc[2][0])+", b= indiferente")
#print (tec)
print("---------------------------------------------------------------------")
print("")
print("")
#Señal sierra
a0s=A
for n in range(1,armonicos+1):
    bs.append(-A/(n*np.pi))
#print (b)
ys=A/2
for n in range(1,armonicos+1):
    ys=ys+bs[n]*np.sin((np.pi*n*t)/T)
    fs.append((np.pi*n)/T)
#y=b[1]*np.sin((np.pi*1*2*t)/T)+b[2]*np.sin((np.pi*2*2*t)/T)+b[3]*np.sin((np.pi*3*2*t)/T)+b[4]*np.sin((np.pi*4*2*t)/T)+b[5]*np.sin((np.pi*5*2*t)/T)+b[6]*np.sin((np.pi*2*6*t)/T)+b[7]*np.sin((np.pi*7*2*t)/T)

print("Armonicos para diente de sierra con frecuencia: "+str(f)+"Hz")
print("Armónicos relacionados a Bn")
for x in range (1,11):
    print(str(x)+" Armonico, b["+str(x)+"]= "+str(bs[x])+" y frecuencia:"+str(fs[x]))
    print("Solucion en TE10")
    te10(fs[x],bs[x],1)
    print(" Constante de propagación: "+str(tes[x][2]))
    print(" Impedancia: "+str(tes[x][3]))
    print(" Velocidad: "+str(tes[x][4]))
    print("Soluciones TM10")
    tm10(fs[x],bs[x],1)
    print(" Constante de propagación: "+str(tms[x][2]))
    print(" Impedancia: "+str(tms[x][3]))
    print(" Velocidad: "+str(tms[x][4]))
    print("")



print("Características de la guia de onda, TE10, frecuencia de corte=16Ghz  a="+str(tec[2][0])+", b= indiferente")
print("Características de la guia de onda, TM10, frecuencia de corte=16Ghz  a="+str(tmc[2][0])+", b= indiferente")
print("---------------------------------------------------------------------")
print("")
print("")
#Señal triangular
a0t=A
for n in range(1,armonicos+1):
    at.append(((-4*A)/(((np.pi)**2)*(((2*n)-1)**2))))
#print (a)
yt=a0t/2
for n in range(1,armonicos+1):  
    yt=yt+at[n]*np.cos((np.pi*((2*n)-1)*t)/T)
    ft.append((np.pi*((2*n)-1))/T)


print("Armonicos para señal triangular con frecuencia: "+str(f)+"Hz")    
for x in range (1,11):
    print(str(x)+" Armonico, a["+str(x)+"]= "+str(at[x])+" y frecuencia:"+str(ft[x]))
    print("Solucion en TE10")
    te10(ft[x],at[x],2)
    print(" Constante de propagación: "+str(tet[x][2]))
    print(" Impedancia: "+str(tet[x][3]))
    print(" Velocidad: "+str(tet[x][4]))
    print("Soluciones TM10")
    tm10(ft[x],at[x],2)
    print(" Constante de propagación: "+str(tmt[x][2]))
    print(" Impedancia: "+str(tmt[x][3]))
    print(" Velocidad: "+str(tmt[x][4]))
    print("")


print("Características de la guia de onda, TE10, frecuencia de corte=16Ghz  a="+str(tec[2][0])+", b= indiferente")
print("Características de la guia de onda, TM10, frecuencia de corte=16Ghz  a="+str(tmc[2][0])+", b= indiferente")

print("---------------------------------------------------------------------")

print("Tomando en cuenta los campos resultantes para estos modos los vectores de poynting serían los siguientes:")
print("Vector de poynting para modo TM10= 0 ya que todos los campos transversales y longitudinales son cero")
print("Vector de poynting para modo TE10=-ΣEy*Hx(k)")

#Metodo para graficar campos longitudinales (onda,modo) onda: 0=cuadrada 1=sierra 2=triangular
#Modo 0=TE 1=TM
#graficarlon(2,0)

#Metodo para graficar transversales (onda,modo,campo) campo=[ex,ey,hx,hy]
#graficartran(2,0,2)

#metodo para graficar comparaciones en 10 armonicos (onda,modo,periodo)
#grafcomp(2,1,T)

#y=b[1]*np.sin((np.pi*1*2*t)/T)+b[2]*np.sin((np.pi*2*2*t)/T)+b[3]*np.sin((np.pi*3*2*t)/T)+b[4]*np.sin((np.pi*4*2*t)/T)+b[5]*np.sin((np.pi*5*2*t)/T)+b[6]*np.sin((np.pi*2*6*t)/T)+b[7]*np.sin((np.pi*7*2*t)/T)
#t = np.arange(0.0, 3.0, 0.1)

#plt.plot(t,ys)
#plt.show()



