# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:57:59 2022

@author: jonas
"""

from numpy import sin, cos, pi

def Sphere2Cartesian(r, theta, phi):
    
    x = r*cos(phi)*sin(theta);
    y = r*sin(phi)*sin(theta);
    z = r*cos(theta);
    
    return x, y, z


import numpy as np

N = 10;

r = np.ones(N);
theta = np.linspace(0, pi, N)
phi = np.zeros(N)

x, y, z = Sphere2Cartesian(r, theta, phi);


import matplotlib.pyplot as plt
'''
fig = plt.figure();
ax = fig.add_subplot(projection='3d');
ax.scatter(X, Y, Z);
plt.show()
'''

def Stereographic(x, y, z):
    epsilon = x/(1 - z);
    eta = y/(1 - z);
    
    return epsilon, eta
    
epsilon, eta = Steriographic(x, y, z);

plt.scatter(epsilon**(-), eta);
plt.show()
    
    


