
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from packing_routines import InitialTangent, SimplePacking
from domains import InBox
from circle import circle, ShowCircles, ShowCirclesOnCylinder
from numpy import pi

# %% Cylinder

#SimplePacking(Circs, CTaC, InRectangle, r_min = 0.2, r_max = 2)

tol = 1e-4;

# Initial circles
initialR = pi/16
Circs = [
    circle(initialR, 0, initialR),
    circle(initialR, 0, 3*initialR),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, InBox, t_min = pi/64, t_max = pi/8, tol=tol)

ShowCircles(Circs, 'cylinder_packing')

#ShowCirclesOnCylinder(Circs)

def projectIntoPlane(Circs, filename=""):
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    for C in Circs:

        theta = np.linspace(0, 2*pi, 100, endpoint=True)
    
        u = C.x + C.r*np.cos(theta)
        v = C.y + C.r*np.sin(theta)
        
        x, y, z = np.cos(u), np.sin(u), v
        
        above_plane = x>0
        plt.plot(y[above_plane], z[above_plane], color='black', lw=0.2)
    
    plt.axis('off');
    plt.gca().set_aspect('equal', adjustable='box')
    if len(filename) > 0:
        plt.savefig(filename + '.svg', format='svg', bbox_inches="tight")
    plt.show()