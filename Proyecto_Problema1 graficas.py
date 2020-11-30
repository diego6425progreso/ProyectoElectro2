#Programa para graficar campos problema 1, para usar descomentar seccion requerida
#Diego Contreras/Ruben Lima/ Diego de Leon
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math
#if using a Jupyter notebook, include:
#matplotlib inline

"""
#Modo TE10
a=0.0125
b=1
x = np.outer(np.linspace(0,a, 30), np.ones(30))
#y = x.copy().T # transpose
y = (np.outer(np.linspace(0,b,30),np.ones(30))).T
cpro=151.03
m=1
n=0
Ex=20
zeta=2
atenuacion=math.exp(-zeta*cpro)
#Frecuencias mayores
z = Ex*np.cos((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Frecuencias menores
#z = Ex*np.cos((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*atenuacion

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')


# Plot a 3D surface
#ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
#ax.contour3D(x, y, z, 50, cmap='binary')
ax.plot_wireframe(x, y, z, color='black')
#ax.plot_wireframe(x, y, z1, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()



#Modo TM11
a=0.2
b=0.01252
x = np.outer(np.linspace(0, a, 30), np.ones(30))
#y = x.copy().T # transpose
y = (np.outer(np.linspace(0,b,30),np.ones(30))).T
cpro=151.03
m=1
n=1
Ex=20
zeta=2
atenuacion=math.exp(-zeta*cpro)
#Frecuencias mayores
z = Ex*np.sin((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Frecuencias Menores
#z = Ex*np.sin((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*atenuacion
#z1 = (Ex*np.sin((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*(zeta+1)))*0

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')


# Plot a 3D surface
#ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
#ax.contour3D(x, y, z, 50, cmap='binary')
ax.plot_wireframe(x, y, z, color='black')
#ax.plot_wireframe(x, y, z1, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


#Modo TE21
a=0.2
b=0.0126
x = np.outer(np.linspace(0,a, 30), np.ones(30))
#y = x.copy().T # transpose
y = (np.outer(np.linspace(0,b,30),np.ones(30))).T
cpro=151.03
m=2
n=1
Ex=20
zeta=0
atenuacion=math.exp(-zeta*cpro)
#Frecuencias Altas
z = Ex*np.cos((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Frecuencias Bajas
#z = Ex*np.cos((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*atenuacion

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')


# Plot a 3D surface
#ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
#ax.contour3D(x, y, z, 50, cmap='binary')
ax.plot_wireframe(x, y, z, color='black')
#ax.plot_wireframe(x, y, z1, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
"""

#Campos transversales
a=0.2
b=0.0126
x = np.outer(np.linspace(0,a, 30), np.ones(30))
#y = x.copy().T # transpose
y = (np.outer(np.linspace(0,b,30),np.ones(30))).T
cpro=151.03
m=2
n=1
ex=251.13
ey=31.64
hx=251.13
hy=34.31
zeta=0
atenuacion=math.exp(-zeta*cpro)
#Para frecuencias altas
#Para ex
#z = ex*np.cos((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Para ey
#z = ey*np.sin((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Para hx
#z = hx*np.sin((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)
#Para hy
z = hy*np.cos((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*zeta)

#Para frecuencias bajas
#Para ex
#z = ex*np.cos((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*zeta)*atenuacion
#Para ey
#z = ey*np.sin((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)*atenuacion
#Para hx
#z = hx*np.sin((math.pi*x*m)/a)*np.cos((math.pi*y*n)/b)*np.cos(-cpro*zeta)*atenuacion
#Para hy
#z = hy*np.cos((math.pi*x*m)/a)*np.sin((math.pi*y*n)/b)*np.cos(-cpro*zeta)*atenuacion

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')


# Plot a 3D surface
#ax.plot_surface(x, y, z,cmap=cm.coolwarm,linewidth=0, antialiased=False)
#ax.contour3D(x, y, z, 50, cmap='binary')
ax.plot_wireframe(x, y, z, color='black')
#ax.plot_wireframe(x, y, z1, color='black')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()



