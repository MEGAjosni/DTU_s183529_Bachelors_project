import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from compute_geodesic_circle import geodesicCircle
from packing_routines import packOnSurface
from circle import circle, tangentPairs
from visualization import displayGeodesicCirclesInDomain, displayGeodesicCirclesOnSurface
from numpy import pi
import matplotlib.pyplot as plt

# %% Torus
from surfaces import torusR, torusODEsystem, torusG

# Initial circles
Circs = [
    circle([0,0], pi/12, torusODEsystem, torusG),
    circle([pi/9, 0], pi/12, torusODEsystem, torusG),
];

CTaC = tangentPairs(Circs, torusODEsystem, torusG)

packOnSurface(Circs, CTaC, ODEsys=torusODEsystem, G=torusG, maxit=10)

displayGeodesicCirclesInDomain(Circs)
displayGeodesicCirclesOnSurface(Circs, torusR)


# %% Sphere
from surfaces import sphereR, sphereODEsystem, sphereG

# Initial circles
Circs = [
    circle([0,pi/2], pi/18, sphereODEsystem, sphereG),
    circle([pi/9, pi/2], pi/18, sphereODEsystem, sphereG),
];

CTaC = tangentPairs(Circs, sphereODEsystem, sphereG)

packOnSurface(Circs, CTaC, u_range=[-pi, pi], v_range=[0, pi], r_min=pi/36, r_max=pi/18, ODEsys=sphereODEsystem, G=sphereG, maxit=10)

displayGeodesicCirclesInDomain(Circs)
displayGeodesicCirclesOnSurface(Circs, sphereR)
