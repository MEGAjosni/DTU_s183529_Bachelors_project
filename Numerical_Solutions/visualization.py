import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def displayGeodesicCirclesInDomain(Circs, filename=""):
    for C in Circs:
        plt.plot(C.coords[:, 0], C.coords[:, 1], color='b')

    plt.gca().set_aspect('equal', adjustable='box')
    if len(filename) > 0:
        plt.savefig('graphix/' + filename + '.svg', format='svg')
    plt.show()
    
    
def displayGeodesicCirclesOnSurface(Circs, parametrization):
    fig = make_subplots()

    # Plot surface
    u = np.linspace(0, 2*np.pi, 100)
    v = np.linspace(0, 2*np.pi, 100)
    u, v = np.meshgrid(u, v)

    x, y, z = parametrization(u,v)

    fig.add_trace(go.Surface(x=x, y=y, z=z, showscale=False))

    # Plot circles on surface
    for C in Circs:

        u = C.coords[:, 0];
        v = C.coords[:, 1];
        
        x, y, z = parametrization(u, v)
        
        fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='black'))


    fig.show(renderer="browser")