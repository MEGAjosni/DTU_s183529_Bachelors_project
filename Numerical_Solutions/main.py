import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from packing_routines import packOnSurface
from circle import circle, tangentPairs
from visualization import displayGeodesicCirclesInDomain, displayGeodesicCirclesOnSurface, projectIntoPlane
from numpy import pi

# %% Torus
from surfaces import torusR, torusODEsystem, torusG

# Initial circles
Circs = [
    circle([0,0], pi/12, torusODEsystem, torusG),
    circle([pi/9, 0], pi/12, torusODEsystem, torusG),
];

CTaC = tangentPairs(Circs, torusODEsystem, torusG)

packOnSurface(Circs, CTaC, r_min=pi/36, r_max=pi/12, ODEsys=torusODEsystem, G=torusG)

displayGeodesicCirclesInDomain(Circs, filename="torus_geodesic_packing")
projectIntoPlane(Circs, torusR, filename="torus_projected")
displayGeodesicCirclesOnSurface(Circs, torusR)

# %% Sphere
from surfaces import sphereR, sphereODEsystem, sphereG

# Initial circles
Circs = [
    circle([0,pi/2], pi/12, sphereODEsystem, sphereG),
    circle([pi/6, pi/2], pi/12, sphereODEsystem, sphereG),
];

CTaC = tangentPairs(Circs, sphereODEsystem, sphereG)

packOnSurface(Circs, CTaC, u_range=[-pi, pi], v_range=[0, pi], r_min=pi/36, r_max=pi/12, ODEsys=sphereODEsystem, G=sphereG)

displayGeodesicCirclesInDomain(Circs, filename="sphere_geodesic_packing")
projectIntoPlane(Circs, sphereR, filename="sphere_projected")
displayGeodesicCirclesOnSurface(Circs, sphereR)

# %% Quadratic surface
from surfaces import quadraticR, quadraticODEsystem, quadraticG

# Initial circles
Circs = [
    circle([0,pi/12.5], pi/12, quadraticODEsystem, quadraticG),
    circle([0,-pi/12.5], pi/12, quadraticODEsystem, quadraticG),
];

CTaC = tangentPairs(Circs, quadraticODEsystem, quadraticG)

packOnSurface(Circs, CTaC, u_range=[-pi/2, pi/2], v_range=[-pi/2, pi/2], r_min=pi/36, r_max=pi/12, ODEsys=quadraticODEsystem, G=quadraticG)

displayGeodesicCirclesInDomain(Circs, filename="quadratic_geodesic_packing")
projectIntoPlane(Circs, quadraticR, filename="quadratic_projected")
displayGeodesicCirclesOnSurface(Circs, quadraticR, u_range=[-pi/2, pi/2], v_range=[-pi/2, pi/2])