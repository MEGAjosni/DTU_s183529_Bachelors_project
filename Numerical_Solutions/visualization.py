'''
#####################################
##### >>>>> Visualization <<<<< #####
#####################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022

Description
-----------
    This script defines functions for illustrating geodesic circle packings.
'''

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def displayGeodesicCirclesInDomain(Circs, filename=""):
    '''
    Description
    -----------
        Makes a plot of a packing's geodesic circles in the parameterdomain.

    Parameters
    ----------
    Circs : list
        Circles in packing.
    filename : string, optional
        If specified, the plot is saved as an svg file with this name. The default is "".

    Returns
    -------
    None.
    '''
    
    # Plot geodesic circles
    for C in Circs:
        plt.plot(C.coords[:, 0], C.coords[:, 1], color='black', lw=0.2)

    # Set layout
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off');
    
    # Save plot
    if len(filename) > 0:
        plt.savefig('graphix/' + filename + '.svg', format='svg', bbox_inches="tight")
    
    plt.show()
    
    return
    
    
def displayGeodesicCirclesOnSurface(Circs, parametrization, u_range=[-np.pi, np.pi], v_range=[-np.pi, np.pi]):
    '''
    Description
    -----------
        Makes a 3D plot of a circle packing on the surface itself.    

    Parameters
    ----------
    Circs : list
        Circles in packing.
    parametrization : function
        Parametrization of surface.
    u_range : list, optional
        Range of the u parameter. The default is [-pi, pi].
    v_range : list, optional
        Range of the v parameter. The default is [-pi, pi].

    Returns
    -------
    None.
    '''
    
    fig = make_subplots()

    # Plot surface
    u = np.linspace(u_range[0], u_range[1], 100)
    v = np.linspace(u_range[0], u_range[1], 100)
    u, v = np.meshgrid(u, v)

    x, y, z = parametrization(u,v)

    colors = np.zeros(shape=x.shape) 
    
    fig.add_trace(go.Surface(x=x, y=y, z=z, showscale=True, surfacecolor=colors, colorscale='RdBu', lighting=dict(ambient=.5)))

    # Plot circles on surface
    for C in Circs:

        u = C.coords[:, 0];
        v = C.coords[:, 1];
        
        x, y, z = parametrization(u, v)
        
        fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='black'))

    # Set layout
    fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)
    fig['layout'].update(scene=dict(aspectmode="data"))
    
    fig.show(renderer="browser")
    
    return

def projectIntoPlane(Circs, parametrization, filename=""):
    '''
    Description
    -----------
        Plots a projection of all points above z=0 into the xy-plane.

    Parameters
    ----------
    Circs : list
        Circles in packing.
    parametrization : function
        Parametrization of surface.
    filename : string, optional
        If specified, the plot is saved as an svg file with this name. The default is "".

    Returns
    -------
    None.
    '''
    
    # Plot circles
    for C in Circs:
        u = C.coords[:, 0];
        v = C.coords[:, 1];
        
        x, y, z = parametrization(u, v)
        
        above_plane = z>0
        plt.plot(x[above_plane], y[above_plane], color='black', lw=0.2)
    
    # Set layout
    plt.axis('off');
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Save plot
    if len(filename) > 0:
        plt.savefig('graphix/' + filename + '.svg', format='svg', bbox_inches="tight")
    
    plt.show()
    
    return
    
    
