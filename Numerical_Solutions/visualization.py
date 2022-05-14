import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def displayGeodesicCirclesInDomain(Circs, filename=""):
    for C in Circs:
        plt.plot(C.coords[:, 0], C.coords[:, 1], color='black', lw=0.2)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off');
    if len(filename) > 0:
        plt.savefig('graphix/' + filename + '.svg', format='svg', bbox_inches="tight")
    plt.show()
    
    
def displayGeodesicCirclesOnSurface(Circs, parametrization, u_range=[-np.pi, np.pi], v_range=[-np.pi, np.pi]):
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

    fig.update_scenes(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False)
    fig['layout'].update(scene=dict(aspectmode="data"))
    fig.show(renderer="browser")
    

def projectIntoPlane(Circs, parametrization, filename=""):
    
    for C in Circs:
        u = C.coords[:, 0];
        v = C.coords[:, 1];
        
        x, y, z = parametrization(u, v)
        
        above_plane = z>0
        plt.plot(x[above_plane], y[above_plane], color='black', lw=0.2)
    
    plt.axis('off');
    plt.gca().set_aspect('equal', adjustable='box')
    if len(filename) > 0:
        plt.savefig('graphix/' + filename + '.svg', format='svg', bbox_inches="tight")
    plt.show()
    
    
