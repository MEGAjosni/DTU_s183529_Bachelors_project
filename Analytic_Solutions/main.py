# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:19:56 2022

@author: jonas
"""

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from numpy import pi
from packing_routines import InitialTangent, SimplePacking, SimplePackingSphere
from domains import InBall, InBox, InBinary, InBallSphere
from circle import circle, ShowCircles, ShowCirclesOnSphere

# %% Fixed circle size in rectangular domain

tol = 1e-4;
r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

CTaC = InitialTangent(Circs);
SimplePacking(Circs, CTaC, InBox, t_min = r, t_max = r, tol=tol)

ShowCircles(Circs, 'fixed_size_inbox')

# %% Variable size in rectangular domain

tol = 1e-4;
r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

CTaC = InitialTangent(Circs);
SimplePacking(Circs, CTaC, InBox, t_min = r/15, t_max = r, tol=tol)

ShowCircles(Circs, 'variable_size_inbox')

# %% Variable size in circular domain

tol = 1e-4;
r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

CTaC = InitialTangent(Circs);
SimplePacking(Circs, CTaC, InBall, t_min = r/15, t_max = r, tol=tol)

ShowCircles(Circs, 'variable_size_inball')

# %% Different initial size in circular domain

tol = 1e-4;
r = 0.15

# Initial circles
Circs = [
    circle(r/2, 0, r/2),
    circle(r, 0, -r),
];

CTaC = InitialTangent(Circs);
SimplePacking(Circs, CTaC, InBall, t_min = r/15, t_max = r, tol=tol)

ShowCircles(Circs, 'diff_ini_size_inball')


# %% Obstacles  in circular domain

tol = 1e-4;
r = 0.15

# Initial circles
Circs = [
    circle(2*r, 2*r, 2*r),
    circle(r/2, 0, r/2),
    circle(r/2, 0, -r/2),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, InBall, t_min = r/15, t_max = r, tol=tol)

ShowCircles(Circs, 'obstacles_inball')

# %% Binary DTU

tol = 1e-4;

# Initial circles
Circs = [
    circle(5, 5, 5),
    circle(5, 5, 15),
    circle(5, 40, 225),
    circle(5, 40, 235),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, InBinary, t_min = 0.5, t_max = 5, tol=tol)

ShowCircles(Circs, 'dtu_logo')

# %% Binary dino

tol = 1e-4;

# Initial circles
Circs = [
    circle(5, 5, 5),
    circle(5, 5, 15),
];

CTaC = InitialTangent(Circs);

SimplePacking(Circs, CTaC, InBinary, t_min = 0.5, t_max = 5, tol=tol)

ShowCircles(Circs, 'dino2')

# %% Fixed circles on sphere

tol = 1e-4;

# Initial circles
Circs = [
    circle(pi/24, 0, pi/24),
    circle(pi/24, 0, -pi/24),
];

CTaC = InitialTangent(Circs);

SimplePackingSphere(Circs, CTaC, InBallSphere, r_min = pi/12, r_max = pi/12, tol=tol)

domainC = circle(7.5, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'fixed_sphere_stereographic')

ShowCirclesOnSphere(Circs)

# %% Variable circles on sphere

tol = 1e-4;

# Initial circles
Circs = [
    circle(pi/24, 0, pi/24),
    circle(pi/24, 0, -pi/24),
];

CTaC = InitialTangent(Circs);

SimplePackingSphere(Circs, CTaC, InBallSphere, r_min =pi/36, r_max = pi/12, tol=tol)

domainC = circle(7.5, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'variable_sphere_stereographic')

ShowCirclesOnSphere(Circs)