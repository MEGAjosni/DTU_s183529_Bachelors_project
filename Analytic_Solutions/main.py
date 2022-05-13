# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:19:56 2022

@author: jonas
"""

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from packing_routines import InitialTangent, SimplePacking, SimplePackingSphere
from domains import OpenDomain, InBall, InBox, InBinary
from circle import circle, ShowCircles, ShowCirclesOnSphere

# %% Circle

tol = 1e-4;

# Initial circles
Circs = [
    circle(0.1, 0, 0.1),
    circle(0.1, 0, -0.1),
];

CTaC = InitialTangent(Circs);

print(CTaC)

SimplePacking(Circs, CTaC, InBall, t_min = 0.01, t_max = 0.5, tol=tol, max_it=1000)

domainC = circle(5, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'ball')


# %% Binary

tol = 1e-4;

# Initial circles
Circs = [
    circle(5, 5, 5),
    circle(5, 5, 15),
    circle(5, 40, 225),
    circle(5, 40, 235),
];

CTaC = InitialTangent(Circs);

print(CTaC)

SimplePacking(Circs, CTaC, InBinary, t_min = 0.5, t_max = 5, tol=tol)

ShowCircles(Circs, 'binary')


# %% Circles on sphere

tol = 1e-4;

# Initial circles
Circs = [
    circle(0.05, 0, 0.05),
    circle(0.05, 0, -0.05),
];

CTaC = InitialTangent(Circs);

print(CTaC)

SimplePackingSphere(Circs, CTaC, InBall, r_min = 0.1, r_max = 0.1, tol=tol)

domainC = circle(20, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'ball')

ShowCirclesOnSphere(Circs)

# %% Rectangle

#SimplePacking(Circs, CTaC, InRectangle, r_min = 0.2, r_max = 2)

tol = 1e-4;

# Initial circles
Circs = [
    circle(3, 3, 3),
    circle(3, -3, 3),
    circle(3, -3, -3),
    circle(3, 3, -3),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, InBox, t_min = 0.05, t_max = 2, tol=tol)

ShowCircles(Circs, 'box')

# %% Open domain

#SimplePacking(Circs, CTaC, InRectangle, r_min = 0.2, r_max = 2)

tol = 1e-4;

# Initial circles
Circs = [
    circle(1, 0, 1),
    circle(1, 0, -1),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, OpenDomain, r_min = 0.05, r_max = 1, tol=tol, max_it=1000)

ShowCircles(Circs, 'open')













