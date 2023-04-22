from typing import Any

import numpy as np
import matplotlib.pyplot as pylab

from animation import Animate
t = np.arange(0,10,0.01)  #define linerar time vector
x = np.sin(t)             #define circle
y = np.cos(t)

xc = np.sin(t*2)             #define new circle
yc = np.cos(t*2)

# Set a few points
xp = np.array([0,0,1,-1])
yp = np.array([-1,1,0,0])

#simulate a new "phi"
phi = t*2




#Animiation der Punkte und Spline
Animate(xp,yp,x[:-3],y[:-3],xc,yc,t[:-3],phi)
