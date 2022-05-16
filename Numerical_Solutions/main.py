'''
###################################
##### >>>>> Main Script <<<<< #####
###################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022

Description
-----------
    This script tests the geodesic circle packing routine for the torus, sphere and quadratic surface.
'''

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from packing_routines import packOnSurface
from circle import circle
from visualization import displayGeodesicCirclesInDomain, displayGeodesicCirclesOnSurface
from numpy import pi

# %% ########################
##### >>>>> Torus <<<<< #####
#############################
from surfaces import torusR, torusODEsystem, torusG

# Define initial circles
Circs = [
    circle([0,0], pi/12, torusODEsystem, torusG),
    circle([pi/9, 0], pi/12, torusODEsystem, torusG),
];

# Run algorithm
packOnSurface(Circs, r_min=pi/36, r_max=pi/12, ODEsys=torusODEsystem, G=torusG)

# Visualize results
displayGeodesicCirclesInDomain(Circs)
displayGeodesicCirclesOnSurface(Circs, torusR)

# %% #########################
##### >>>>> Sphere <<<<< #####
##############################
from surfaces import sphereR, sphereODEsystem, sphereG

# Define initial circles
Circs = [
    circle([0,pi/2], pi/12, sphereODEsystem, sphereG),
    circle([pi/6, pi/2], pi/12, sphereODEsystem, sphereG),
];

# Run algorithm
packOnSurface(Circs, u_range=[-pi, pi], v_range=[0, pi], r_min=pi/36, r_max=pi/12, ODEsys=sphereODEsystem, G=sphereG)

# Visualize results
displayGeodesicCirclesInDomain(Circs)
displayGeodesicCirclesOnSurface(Circs, sphereR)

# %% ####################################
##### >>>>> Quadratic surface <<<<< #####
#########################################
from surfaces import quadraticR, quadraticODEsystem, quadraticG

# Define initial circles
Circs = [
    circle([0,pi/12.5], pi/12, quadraticODEsystem, quadraticG),
    circle([0,-pi/12.5], pi/12, quadraticODEsystem, quadraticG),
];

# Run algorithm
packOnSurface(Circs, u_range=[-pi/2, pi/2], v_range=[-pi/2, pi/2], r_min=pi/36, r_max=pi/12, ODEsys=quadraticODEsystem, G=quadraticG)

# Visualize results
displayGeodesicCirclesInDomain(Circs)
displayGeodesicCirclesOnSurface(Circs, quadraticR, u_range=[-pi/2, pi/2], v_range=[-pi/2, pi/2])