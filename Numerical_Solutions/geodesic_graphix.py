# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:54:22 2022

@author: jonas
"""

from compute_geodesic_circle import geodesicCircle
import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib
from numpy import cos, sin, sqrt, pi

# Rewrite geodesic equations as first order system.
def torusODEsystem(t, y, R1=1, R2=0.5):
    u, v, du, dv = y
    
    dydt = [
            du,
            dv,
            (2*R2*sin(v)*dv*du) / (R1 + R2*cos(v)),
            -((R1+R2*cos(v))*sin(v)*du*du) / R2
        ]
    dydt = np.array(dydt)
    
    return dydt

def torusG(P, R1=1, R2=0.5):
    G = np.array(
        [
            [(R1 + R2*cos(P[1]))**2, 0],
            [0, R2**2]
            ]
        )
    return G
    

N = 50
P = [0, np.pi/2]
r = np.pi/4

x = []
y = []

for t in np.linspace(0.001, r, 10):
    C = geodesicCircle(P, t, torusODEsystem, torusG)
    x.append(C[:, 0])
    y.append(C[:, 1])

x = np.array(x).T
y = np.array(y).T

for i in range(len(x)):
    plt.plot(x[i], y[i], color='b')

C = geodesicCircle(P, r, torusODEsystem, torusG)
plt.plot(C[:, 0], C[:, 1], color='r')
tikzplotlib.save("numeric_geodesic.tex")

plt.show()