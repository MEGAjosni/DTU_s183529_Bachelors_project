'''
Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def ShowCircles(Circs, filename=""):
    '''
    Description
    -----------
        Makes a plot of a circle packing.

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
    
    # Lets draw a circle
    fig, ax = plt.subplots();
    ax.set_aspect(1);
    
    # Display circles
    for i, C in enumerate(Circs):
        # plt.text(C.x, C.y, i, size=C.r, ha='center', va='center')
        circ = C.show();
        ax.add_artist(circ);
    
    # Set axis range    
    x_lower = min([C.x - C.r for C in Circs]);
    x_upper = max([C.x + C.r for C in Circs]);
    
    y_lower = min([C.y - C.r for C in Circs]);
    y_upper = max([C.y + C.r for C in Circs]);
    
    plt.xlim([x_lower, x_upper]);
    plt.ylim([y_lower, y_upper]);
    
    plt.axis('off');
    
    # Save and display plot
    if len(filename) != 0:
        plt.savefig("graphix/" + filename + '.svg', format='svg', bbox_inches="tight")
    plt.show();
    
    
def ShowCirclesOnSphere(Circs):
    '''
    Description
    -----------
        Stereographically projects circles onto the unit sphere.

    Parameters
    ----------
    Circs : list
        Circles in packing.

    Returns
    -------
    None.
    '''
    
    fig = make_subplots()
    
    # Plot circles on sphere
    for C in Circs:
        
        x, y, z = C.StereographicProjection()
        
        fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='black'))
    
    # Plot sphere
    r = 1

    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)

    x = r * np.outer(np.cos(theta),np.sin(phi))
    y = r * np.outer(np.sin(theta),np.sin(phi))
    z = r * np.outer(np.ones(100),np.cos(phi))
    
    colors = np.zeros(shape=x.shape) 
    
    fig.add_trace(go.Surface(x=x, y=y, z=z, showscale=False, surfacecolor=colors, colorscale='RdBu', lighting=dict(ambient=.5)))
    fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)
    
    fig.show(renderer="browser")