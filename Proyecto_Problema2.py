#Programa para obtencion de datos brutos problema 2
#Diego Contreras/Ruben Lima/Diego de Leon
import math
f=float(input("Ingrese frecuencia deseada en GHz"))
fc=float(input("Ingrese la frecuencia de corte en GHz"))
print("Frecuencia de corte elegida: "+str(fc/1e9))
f=f*10**9
w=2*math.pi*f
fc=fc*10**9
e=8.84*10**-12
u=1.26*10**-6
m=1
n=1
c=3e8
a=1
b=1
beta=1
cpro=1
ntm=0
nte=0
ez=20
x11=3.832
x10=3.832
yo=(c/f)
yg=1
frec=(fc/f)
Impm=0;
ez=1
A=1
B=1
phi=1
cpc=False
n=1
m=1
a=0.2
if(f>fc):
#Modo TE: x,beta,vel,long
    
    
 
    a=x11/(2*fc*math.pi*((u*e)**0.5))    
    
    #constante de  propagacion
    cpro=(((w**2*u*e)-((x11/a)**2))**0.5)
    
    
    f1=(w**2)*u*e
    f1d=w*w*u*e
    f2=((3.832/0.02287)**2)
    f3=f1-f2
    f4=(f3)**0.5
    ntm=(cpro)/(w*e)
    
    nte=(w*u)/(cpro)
    
    #velocidad de fase
    vel=(1/(u*e)**0.5)/(((1-(fc/f)**2))**0.5)
    
    
    long=(yo/(1-(fc/f)**2)**0.5)
    vel=round(vel,2)
    long=round(long,5)
    cpc=True
#Modo TM: x
    
    #impedanc
    Impm=(w*u/cpro)
#Falta que es y0 y yg.     
    
    
    #campos longitudinales
    
    ez= (A*math.sin(a*phi)+B*math.cos(n*phi))*x11
    

elif f==fc:
    cpro=0
    ntm=0
    nte=0
    vel="no aplica"
    long="no aplica"
    cpc=False
else:
    cpro=(w/c)*((((fc/f)**2)-1)**0.5)
    ntm=(cpro)/(w*e)
    nte=(w*u)/cpro
    vel="no aplica"
    long="no aplica"
    cpc=False
cpro1=cpro*1j
kc=cpro1**2+(w**2)*u*e


cpro=round(cpro,2)
nte=round(nte,2)
ntm= round(ntm,2)
print("")
print("Para modo TM11:")
#a=float((((float(m)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(n)*math.pi)/float(b))**2)))**0.5)
a=x11/(2*fc*math.pi*((u*e)**0.5))
a=round(a,5)
print("El valor de 'a' es: "+str(a))
print("El valor de 'b' es indiferente")
print("Constante de propagacion: "+str(cpro))

#print("w: "+str(w))
#print("1a parte: "+str(f1))
#print("1ra w*w: "+str(f1d))
#print("2a parte: "+str(f2))
#print("3ra parte: "+str(f3))
#print("4ta parte: "+str(f4))

print("Impedancia intrinseca: "+str(nte))
print("La velocidad de fase es: "+str(vel))
print("La longitud de onda es: "+str(long))
print("")
print("Campos Longitudinales :")
print("  ")
print("H(z)=0")
print("  ")

if(cpc==True):
    
    
   print("Suponiendo que A es constante")
   print("Suponiendo que B es constante")
   print("suponiendo que n = 1 ")
   print("sabemos que Jn(Kc p)= Bessel tipo 1")
   print("")
   print("")
    
   print("ez(ϕ,p,z)= "+str(A) +"Sin("+str(n)+"Φ )+ B cos("+str(n)+"Φ)*""Jc(Kc P)")
   #print("e(z)="+str(ez))
    
else:
    print("ez(ϕ,p,z)= "+str(A) +"Sin("+str(n)+"Φ )+ B cos("+str(n)+"Φ)*""Jc(Kc P)")
    print("")
    print("Campos transversales: ")

kc2=w**2*u*e-cpro**2

A=1
B=1

ex=((-1j*cpro)/(kc2))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
ey=((-1j*cpro*n)/(kc2*a))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
hx=((1j*w*n*e)/(kc2*a))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
hy=((-1j*w*e)/(kc))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11

ex=abs(ex)
ey=abs(ey)
hx=abs(hx)
hy=abs(hy)

print("  ")
print("  ")
print("Campos transversales: ")
print("  ")

if(ex==0):
    print("Ep(ϕ,p,z)=0")
else:
    ex=round(ex,8)
   # print("E(p)="+str(ex))
    print("Ep(ϕ,p,z)=(-j*B/Kc^2(("+str(A)+"sin("+str(n)+"phi) +"+str(B)+"Cos("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
if(ey==0):
    print("Eϕ(ϕ,p,z)=0")
else:
    ey=round(ey,8)
    print("Eϕ(ϕ,p,z)=(-j*B/Kc^2*p(("+str(A)+"cos("+str(n)+"phi) +"+str(B)+"sin("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
if(hx==0):
    print("Hp(ϕ,p,z)=0")
else:
    hx=round(hx,8)
    print("Hp(ϕ,p,z)=(j*w*E*n/Kc^2*p(("+str(A)+"cos("+str(n)+"phi) +"+str(B)+"sin("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
if(hy==0):
    print("Hϕ(ϕ,p,z)=0")
else:
    hy=round(hy,8)
    print("Hϕ(ϕ,p,z)=(-j*w*E*n/Kc(("+str(A)+"sin("+str(n)+"phi) +"+str(B)+"cos("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    




print("----------------------------------------------------")


print("")

print("Para modo TE01:")
print("  ")

b=float((((float(n)*math.pi)**2)/((((2*math.pi*float(fc))/float(c))**2)-(((float(m)*math.pi)/float(a))**2)))**0.5)
b=round(b,5)
print("El valor de 'a' se fijo a "+str(a))
print("El valor de 'b' es: no aplica")
print("Constante de propagacion: "+str(cpro))
print("Impedancia intrinseca: "+str(ntm))
print("La velocidad de fase es: "+str(vel))
print("La longitud de onda es: "+str(long))
print("")
print("Campos longitudinales:")
print("  ")
print("ez(ϕ,p,z)=0")
print("  ")




if(cpc==True):
     print("hz(ϕ,p,z)= "+str(A) +"Sin("+str(n)+"Φ )+ B cos("+str(n)+"Φ)*""Jc(Kc P)*")
     print("")
else:
  print("hz(ϕ,p,z)= "+str(A) +"Sin("+str(n)+"Φ )+ B cos("+str(n)+"Φ)*""Jc(Kc P)")
  print("")
print("Campos transversales: ")

print("")
ex=((-1j*cpro)/(kc2))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
ey=((-1j*cpro*n)/(kc2*a))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
hx=((1j*w*n*e)/(kc2*a))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11
hy=((-1j*w*e)/(kc))*(A*math.sin(a*phi)+B*math.cos(n*phi))*x11


ex=abs(ex)
ey=abs(ey)
hx=abs(hx)
hy=abs(hy)


if(ex==0):
    print("Ep(ϕ,p,z)=0")
else:
    ex=round(ex,5)
    print("Ep(ϕ,p,z)=(-j*B/Kc^2(("+str(A)+"sin("+str(n)+"phi) +"+str(B)+"Cos("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
    
if(ey==0):
    print("Eϕ(ϕ,p,z)=0")
else:
    ey=round(ey,5)
    print("Eϕ(ϕ,p,z)=(-j*B/Kc^2*p(("+str(A)+"cos("+str(n)+"phi) +"+str(B)+"sin("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
if(hx==0):
    print("Hp(ϕ,p,z)=0")
else:
    hx=round(hx,5)
    print("Hp(ϕ,p,z)=(j*w*E*n/Kc^2*p(("+str(A)+"cos("+str(n)+"phi) +"+str(B)+"sin("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
if(hy==0):
    print("Hϕ(ϕ,p,z)=0")
else:
    print("Hϕ(ϕ,p,z)=(-j*w*E*n/Kc(("+str(A)+"sin("+str(n)+"phi) +"+str(B)+"cos("+str(n)+"phi))*"+"Jn(Kc p)*e^-jBz")
    
    
    

print("----------------------------------------------------")
print("")

print ("Vectores de poynting")
print("Modo TE")
print("Vector=((Eϕ*Hz)/p)(p)-Ep*Hz(ϕ)+(Ep*Hϕ-((Eϕ*Hp)/p))(z)")
print("Modo TM")
print("Vector=-Ez*Hϕ(p)+Ez*Hp(ϕ)+(Ep*Hϕ-((Eϕ*Hp)/p))(z)")



