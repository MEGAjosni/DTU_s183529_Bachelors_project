'''
#####################################
##### >>>>> Demonstration <<<<< #####
#####################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022

Description
-----------
    This script makes an illustration of how geodesic circles are approximated.
'''

from compute_geodesic_circle import geodesicCircle
import numpy as np
import matplotlib.pyplot as plt
import tikzplotlib
from surfaces import torusODEsystem, torusG

# Define parameters
N = 50
P = [0, np.pi/2]
r = np.pi/4

# Make approximation
x = []
y = []
for t in np.linspace(0.001, r, 10):
    C = geodesicCircle(P, t, torusODEsystem, torusG)
    x.append(C[:, 0])
    y.append(C[:, 1])

x = np.array(x).T
y = np.array(y).T

# Plot results
for i in range(len(x)):
    plt.plot(x[i], y[i], color='b')
C = geodesicCircle(P, r, torusODEsystem, torusG)
plt.plot(C[:, 0], C[:, 1], color='r')
tikzplotlib.save("numeric_geodesic.tex")
plt.show()