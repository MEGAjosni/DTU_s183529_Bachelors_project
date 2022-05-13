# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:19:56 2022

@author: jonas
"""

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

ShowCircles(Circs, 'box')

ShowCirclesOnCylinder(Circs)
