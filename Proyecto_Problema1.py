#Programa para ejecutar obtencion de datos brutos problema 1
#Diego Contreras/Ruben Lima/Diego de Leon
import math
f=float(input("Ingrese frecuencia deseada en GHz"))
fc=float(input("Ingrese la frecuencia de corte en GHz"))
print("Frecuencia de corte elegida: "+str(fc/1e9))
f=f*1e9
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

print("")
print("Para modo TE10:")
a=float((((float(m)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(n)*math.pi)/float(b))**2)))**0.5)
a=round(a,5)
print("El valor de 'a' es: "+str(a))
print("El valor de 'b' es indiferente")
print("Constante de propagacion: "+str(cpro))
print("Impedancia intrínseca: "+str(nte))
print("La velocidad de fase es: "+str(vel))
print("La longitud de onda es: "+str(long))
print("")
print("Campos Longitudinales")
print("E(z)=0")
if(cpc==True):
    print("H(z)="+str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")cos(-"+str(cpro)+"z)")
    h_z=str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")cos(-"+str(cpro)+"z)"
else:
    print("H(z)="+str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")e^-z"+str(cpro))
    h_z=str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")e^-z"+str(cpro)
print("")
print("Campos transversales: ")
ex=((1j*w*u*n*math.pi)/(kc*b))*ez
ey=((-1j*w*u*m*math.pi)/(kc*a))*ez
hx=((cpro1*m*math.pi)/(kc*a))*ez
print(hx)
hy=((cpro1*n*math.pi)/(kc*b))*ez
ex=abs(ex)
ey=abs(ey)
hx=abs(hx)
hy=abs(hy)
if(ex==0):
    print("E(x)=0")
    e_x=0
else:
    ex=round(ex,2)
    print("E(x)="+str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    e_x=str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"
if(ey==0):
    print("E(y)=0")
    e_y=0
else:
    ey=round(ey,2)
    print("E(y)="+str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    e_y=str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hx==0):
    print("H(x)=0")
    h_x=0
else:
    hx=round(hx,2)
    print("H(x)="+str(hx)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    h_x=str(hx)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hy==0):
    print("H(y)=0")
    h_y=0
else:
    hy=round(hy,2)
    print("H(y)="+str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    h_y=str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"

print("Vector de pointing=("+str(e_y)+")*("+str(h_z)+")(i) -("+str(e_x)+")*("+str(h_z)+")(j) +(("+str(e_x)+")*("+str(h_y)+")-("+str(e_y)+")*("+str(h_x)+")(k)")


print("----------------------------------------------------")

print("")

print("Para modo TM11:")
n=1
m=1
a=0.2
b=float((((float(n)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(m)*math.pi)/float(a))**2)))**0.5)
b=round(b,5)
print("El valor de 'a' se fijó a 0.2")
print("El valor de 'b' es: "+str(b))
print("Constante de propagacion: "+str(cpro))
print("Impedancia intrínseca: "+str(ntm))
print("La velocidad de fase es: "+str(vel))
print("La longitud de onda es: "+str(long))
print("")
print("Campos longitudinales:")
print("H(z)=0")

if(cpc==True):
    print("E(z)="+str(ez)+"sen(π*x*"+str(m)+"/"+str(a)+")*sen(π*y*"+str(n)+"/"+str(b)+")cos(-"+str(cpro)+"z)")
    e_z=str(ez)+"sen(π*x*"+str(m)+"/"+str(a)+")*sen(π*y*"+str(n)+"/"+str(b)+")cos(-"+str(cpro)+"z)"
else:
    print("E(z)="+str(ez)+"sen(π*x*"+str(m)+"/"+str(a)+")*sen(π*y*"+str(n)+"/"+str(b)+")e^-z"+str(cpro))
    e_z=str(ez)+"sen(π*x*"+str(m)+"/"+str(a)+")*sen(π*y*"+str(n)+"/"+str(b)+")e^-z"+str(cpro)
print("")
print("Campos transversales: ")
ex=((cpro1*m*math.pi)/(kc*a))*ez
ey=((cpro1*n*math.pi)/(kc*b))*ez
hx=((w*e*-1j*n*math.pi)/(kc*b))*ez
hy=((w*e*-1j*m*math.pi)/(kc*a))*ez
ex=abs(ex)
ey=abs(ey)
hx=abs(hx)
hy=abs(hy)
if(ex==0):
    print("E(x)=0")
    e_x=0
else:
    ex=round(ex,2)
    print("E(x)="+str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    e_x=str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"
if(ey==0):
    print("E(y)=0")
    e_y=0
else:
    ey=round(ey,2)
    print("E(y)="+str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    e_y=str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hx==0):
    print("H(x)=0")
    h_x=0
else:
    hx=round(hx,2)
    print("H(x)="+str(ex)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    h_x=str(ex)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hy==0):
    print("H(y)=0")
    h_y=0
else:
    hy=round(hy,2)
    print("H(y)="+str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    h_y=str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"

print("Vector de pointing=(-"+str(e_z)+")*("+str(h_y)+")(i) +("+str(e_z)+")*("+str(h_x)+")(j) +(("+str(e_x)+")*("+str(h_y)+")-("+str(e_y)+")*("+str(h_x)+")(k)")
print("----------------------------------------------------")
print("")

print("Para modo TE21:")
n=1
m=2
a=0.2
b=float((((float(n)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(m)*math.pi)/float(a))**2)))**0.5)
b=round(b,5)
print("El valor de 'a' se fijó a 0.2")
print("El valor de 'b' es: "+str(b))
print("Constante de propagacion: "+str(cpro))
print("Impedancia intrínseca: "+str(nte))
print("La velocidad de fase es: "+str(vel))
print("La longitud de onda es: "+str(long))
print("")
print("E(z)=0")
if(cpc==True):
    print("H(z)="+str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")cos(-"+str(cpro)+"z)")
else:
    print("H(z)="+str(ez)+"cos(π*x*"+str(m)+"/"+str(a)+")*cos(π*y*"+str(n)+"/"+str(b)+")e^-z"+str(cpro))
print("")
print("Campos transversales: ")
ex=((1j*w*u*n*math.pi)/(kc*b))*ez
ey=((-1j*w*u*m*math.pi)/(kc*a))*ez
hx=((cpro1*m*math.pi)/(kc*a))*ez
hy=((cpro1*n*math.pi)/(kc*b))*ez
ex=abs(ex)
ey=abs(ey)
hx=abs(hx)
hy=abs(hy)
if(ex==0):
    print("E(x)=0")
    e_x=0
else:
    ex=round(ex,2)
    print("E(x)="+str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    e_x=str(ex)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"
if(ey==0):
    print("E(y)=0")
    e_y=0
else:
    ey=round(ey,2)
    print("E(y)="+str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    e_y=str(ey)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hx==0):
    print("H(x)=0")
    h_x=0
else:
    hx=round(hx,2)
    print("H(x)="+str(ex)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)")
    h_x=str(ex)+"sen(π*"+str(m)+"*x/"+str(a)+")cos(π*y*"+str(n)+"/b)sen(90)"
if(hy==0):
    print("H(y)=0")
    h_y=0
else:
    hy=round(hy,2)
    print("H(y)="+str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)")
    h_y=str(hy)+"cos(π*"+str(m)+"*x/"+str(a)+")sen(π*y*"+str(n)+"/b)sen(90)"


print("Vector de pointing=("+str(e_y)+")*("+str(h_z)+")(i) -("+str(e_x)+")*("+str(h_z)+")(j) +(("+str(e_x)+")*("+str(h_y)+")-("+str(e_y)+")*("+str(h_x)+")(k)")


