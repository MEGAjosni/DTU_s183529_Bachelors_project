'''
Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

from numpy import pi
from packing_routines import SimplePacking, SimplePackingSphere
from domains import InBall, InBox, InBinary, InBallSphere
from circle import circle
from visualization import ShowCircles, ShowCirclesOnSphere

# %% Fixed circle size in rectangular domain

r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

SimplePacking(Circs, InBox, t_min = r, t_max = r)

ShowCircles(Circs, 'fixed_size_inbox')

# %% Variable size in rectangular domain

r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

SimplePacking(Circs, InBox, t_min = r/15, t_max = r)

ShowCircles(Circs, 'variable_size_inbox')

# %% Variable size in circular domain

r = 0.15

# Initial circles
Circs = [
    circle(r, 0, r),
    circle(r, 0, -r),
];

SimplePacking(Circs, InBall, t_min = r/15, t_max = r)

ShowCircles(Circs, 'variable_size_inball')

# %% Different initial size in circular domain

r = 0.15

# Initial circles
Circs = [
    circle(r/2, 0, r/2),
    circle(r, 0, -r),
];

SimplePacking(Circs, InBall, t_min = r/15, t_max = r)

ShowCircles(Circs, 'diff_ini_size_inball')


# %% Obstacles  in circular domain

r = 0.15

# Initial circles
Circs = [
    circle(2*r, 2*r, 2*r),
    circle(r/2, 0, r/2),
    circle(r/2, 0, -r/2),
];

SimplePacking(Circs, InBall, t_min = r/15, t_max = r)

ShowCircles(Circs, 'obstacles_inball')

# %% Binary DTU

# Initial circles
Circs = [
    circle(5, 5, 5),
    circle(5, 5, 15),
    circle(5, 40, 225),
    circle(5, 40, 235),
];

SimplePacking(Circs, InBinary, t_min = 0.5, t_max = 5)

ShowCircles(Circs, 'dtu_logo')

# %% Binary dino

# Initial circles
Circs = [
    circle(5, 5, 5),
    circle(5, 5, 15),
];

SimplePacking(Circs, InBinary, t_min = 0.5, t_max = 5)

ShowCircles(Circs, 'dino2')

# %% Fixed circles on sphere

# Initial circles
Circs = [
    circle(pi/128, 0, pi/128),
    circle(pi/128, 0, -pi/128),
];

SimplePackingSphere(Circs, InBallSphere, r_min = pi/64, r_max = pi/64)

domainC = circle(7.5, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'fixed_sphere_stereographic')

ShowCirclesOnSphere(Circs)

# %% Variable circles on sphere

# Initial circles
Circs = [
    circle(pi/24, 0, pi/24),
    circle(pi/24, 0, -pi/24),
];

SimplePackingSphere(Circs, InBallSphere, r_min =pi/36, r_max = pi/12)

domainC = circle(7.5, 0, 0);
Circs.append(domainC)

ShowCircles(Circs, 'variable_sphere_stereographic')

ShowCirclesOnSphere(Circs)