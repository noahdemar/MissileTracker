# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 08:58:08 2019

@author: Intern
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
time=0
dt=0.1
missilestate=1
def missile(xm,ym,zm):
    xvm=20*np.sin(time/2)
    yvm=2
    zvm=0
    zm=xm+xvm*dt
    ym=ym+yvm*dt
    zm=zm+zvm*dt
    return(xm,ym,zm)

def interceptor(xi,yi,zi):
    viabs=10
    targrange = np.sqrt((xm-xi)**2+(ym-yi)**2+(zm-zi)**2)
    impacttime = targrange/viabs
    print("imapct time:",impacttime,"s")
    xvi=(xm-xi)/targrange
    yvi=(ym-yi)/targrange
    zvi=(zm-zi)/targrange
    xi=xi+xvi*viabs*dt
    yi=yi+yvi*viabs*dt
    zi=zi+zvi*viabs*dt
    return(xi,yi,zi)
xm=100
ym=100
zm=100
xi=0
yi=0
zi=0

xvm=5
yvm=2
zvm=0
xvi=0
yvi=0
zvi=0

c=[]
xmcoords,ymcoords,zmcoords = [],[],[]
xicoords,yicoords,zicoords = [],[],[]

while missilestate == 1 and time<1000:
    time = time+dt
    xm,ym,zm = missile(xm,ym,zm)
    xi,yi,zi = interceptor(xi,yi,zi)
    if np.sqrt((xm-xi)**2+(ym-yi)**2+(zm-zi)**2)<20:
        missilestate=0
        print('Missile intercepted')
    xmcoords.append(xm),ymcoords.append(ym),zmcoords.append(zm)
    xicoords.append(xi),yicoords.append(yi),zicoords.append(zi)  
    c.append(time)
    
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(xmcoords,ymcoords,zmcoords)
ax.scatter(xicoords,yicoords,zicoords,c=c)
ax.scatter(xicoords[-1],yicoords[-1],zicoords[-1],c='r',s=2**10)
