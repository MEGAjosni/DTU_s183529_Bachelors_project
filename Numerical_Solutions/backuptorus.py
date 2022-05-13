# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:26:19 2022

@author: jonas
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 12 01:38:34 2022

@author: jonas
"""

from numpy import pi
import matplotlib.pyplot as plt
from polygon_intersect import intersection
from compute_geodesic import torusGeodesicCircle
import matplotlib.pyplot as plt
import numpy as np

N = 100
r = pi/24

Circs = [];

Circs.append([r, 0, 0])
Circs.append([r, pi/18, 0])

CTaC = [[0, 1]];

maxit = 100

it = 0
while CTaC and it < maxit:
    print(it)
    
    # Get tangent circles
    idx = CTaC.pop(0);
    C1 = Circs[idx[0]];
    C2 = Circs[idx[1]];
    
    # Find new centerpoints
    new_centers = intersection(torusGeodesicCircle(C1[1:3], C1[0]+r), torusGeodesicCircle(C2[1:3], C2[0]+r));
    new_centers = np.array(new_centers).T
    
    new_geodesics = [
        torusGeodesicCircle(new_centers[0], r),
        torusGeodesicCircle(new_centers[1], r),
        ];
    
    for k, poly in enumerate(new_geodesics):
        valid = True;
        for C in Circs:
            inter = intersection(poly, torusGeodesicCircle(C[1:3], C[0]))
            if len(inter[0]) != 0 and C not in [C1, C2]:
                valid = False;
        
        if min(poly[:,0]) < -pi or max(poly[:,0]) > pi or min(poly[:,1]) < -pi or max(poly[:,1]) > pi:
            valid = False;
        
        if valid:
            Circs.append([r, new_centers[k][0], new_centers[k][1]])
            CTaC.append([idx[0], len(Circs)-1])
            CTaC.append([idx[1], len(Circs)-1])
    
    it += 1;


for C in Circs:
    coords = torusGeodesicCircle(C[1:3], C[0])
    plt.plot(coords[:, 0], coords[:, 1], color='b')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()


# Plot torus


import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots



fig = make_subplots()

def r(u, v, r1=1, r2=1/2):
    return (r1 + r2*np.cos(v))*np.cos(u), (r1 + r2*np.cos(v))*np.sin(u), r2*np.sin(v)

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 2*np.pi, 100)
u, v = np.meshgrid(u, v)



x, y, z = r(u,v, r2=1/2-0.005)

fig.add_trace(go.Surface(x=x, y=y, z=z, showscale=False))

for C in Circs:
    geodesic = torusGeodesicCircle(C[1:3], C[0])
    
    u = geodesic[:, 0];
    v = geodesic[:, 1];
    
    x, y, z = r(u, v)
    
    fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='black'))


fig.show(renderer="browser")
