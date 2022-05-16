'''
Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022

Description
-----------
    Parametrization, geodesic equation and metric tensor for selected surfaces.
'''

import numpy as np
from numpy import cos, sin, tan

'''
#############################
##### >>>>> Torus <<<<< #####
#############################
'''
# Torus parametrization
def torusR(u, v, r1=1, r2=1/2): 
    return (r1 + r2*np.cos(v))*np.cos(u), (r1 + r2*np.cos(v))*np.sin(u), r2*np.sin(v)

# Torus geodesic equations
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

# Torus metric tensor
def torusG(P, R1=1, R2=0.5):
    G = np.array(
        [
            [(R1 + R2*cos(P[1]))**2, 0],
            [0, R2**2]
            ]
        )
    return G

'''
##############################
##### >>>>> Sphere <<<<< #####
##############################
'''
# Sphere parametrization
def sphereR(u, v):
    return np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v)

# Sphere geodesic equations
def sphereODEsystem(t, y):
    u, v, du, dv = y
    
    dydt = [
            du,
            dv,
            -2*dv*du/tan(v),
            cos(v)*sin(v)*du**2
        ]
    dydt = np.array(dydt)
    
    
    return dydt

# Sphere metric tensor
def sphereG(P, R1=1, R2=0.5):
    G = np.array(
        [
            [sin(P[1])**2, 0],
            [0, 1]
            ]
        )
    return G

'''
##############################
##### >>>>> Cosine <<<<< #####
##############################
'''
# Quadratic surface parametrization
def quadraticR(u, v):
    return u, v, - u**2 - v**2

# Quadratic surface geodesic equations
def quadraticODEsystem(t, y):
    u, v, du, dv = y
    
    dydt = [
            du,
            dv,
            - (4*u*(du**2 + dv**2)) / (4*u**2 + 4*v**2 + 1),
            - (4*v*(du**2 + dv**2)) / (4*u**2 + 4*v**2 + 1)
        ]
    dydt = np.array(dydt)
    
    
    return dydt

# Quadratic metric tensor
def quadraticG(P, R1=1, R2=0.5):
    G = np.array(
        [
            [4*P[0]**2 + 1, 4*P[0]*P[1]],
            [4*P[0]*P[1], 4*P[1]**2 + 1]
            ]
        )
    return G