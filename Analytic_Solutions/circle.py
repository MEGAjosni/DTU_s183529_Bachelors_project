# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:30:27 2022

@author: jonas
"""

from math import sqrt, cos, sin, pi
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, Eq, solve
import tikzplotlib


class circle:
    
    def __init__(self, r, x, y):
        self.x = x;
        self.y = y;
        self.r = r;

    def overlapping(self, C, tol=1e-4):
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return d < self.r + C.r - tol;
        
    def tangent(self, C, tol=1e-4):
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return abs(d - (self.r + C.r)) <= tol or abs(d - abs(self.r - C.r)) <= tol;

    def intersection(self, C, t=0, tol=1e-4):
        '''
        print(t)
        self.describe()
        C.describe()
        
        x, y = symbols('x y', real=True);
        
        eq1 = Eq((x - self.x)**2 + (y - self.y)**2, (self.r + t)**2)
        eq2 = Eq((x - C.x)**2 + (y - C.y)**2, (C.r + t)**2)

        sol = solve((eq1, eq2), (x, y), manual=True)

        print(sol)

        sol = [list(map(float, s)) for s in sol]

        return sol
        
        '''
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        
        # Expand circle radii by t
        
        if abs(d - (self.r + C.r)) <= tol: 
            r1 = self.r + t;
            r2 = C.r + t;
        elif self.r > C.r:
            r1 = self.r - t;
            r2 = C.r + t;
        else:
            r1 = self.r + t;
            r2 = C.r - t;
        
        
        # Distance between centers
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        
        try:
            A = 1/2*np.array([self.x + C.x, self.y + C.y]) + (r1**2 - r2**2)/(2*d**2) * np.array([C.x - self.x, C.y - self.y]);
            B = 1/2*(sqrt(2*(r1**2 + r2**2)/(d**2) - (r1**2 - r2**2)**2/(d**4) - 1)) * np.array([C.y - self.y, self.x - C.x]);
        except ValueError:
            print("Warning! Circles does not intersect.")
            return [None, None]
            
        p1 = A - B;
        p2 = A + B;
        
        return [p1, p2]
        

    def show(self):
        return plt.Circle((self.x, self.y), self.r, fill=False, lw=0.2);
    
    def StereographicProjection(self):
        
        theta = np.linspace(0, 2*pi, 100, endpoint=True)
        
        X = self.x + np.cos(theta)*self.r
        Y = self.y + np.sin(theta)*self.r     

        x = 2*X / (1 + X**2 + Y**2)
        y = 2*Y / (1 + X**2 + Y**2)
        z = (-1 + X**2 + Y**2) / (1 + X**2 + Y**2)

        return x, y, z


    def describe(self):
        print("r = {}, center = [{}, {}].".format(self.r, self.x, self.y));


def ShowCircles(Circs, fileName=False):

    import matplotlib.pyplot as plt
    
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
    if fileName:
        plt.savefig("graphix/" + fileName + '.svg', format='svg', bbox_inches="tight")
    plt.show();
    
    
def ShowCirclesOnSphere(Circs):
    
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    
    fig = make_subplots()
    
    for C in Circs:
        
        x, y, z = C.StereographicProjection()
        
        fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='white'))
    
    # Plot sphere
    r = 0.99

    theta = np.linspace(0,2*np.pi,100)
    phi = np.linspace(0,np.pi,100)

    x0 = r * np.outer(np.cos(theta),np.sin(phi))
    y0 = r * np.outer(np.sin(theta),np.sin(phi))
    z0 = r * np.outer(np.ones(100),np.cos(phi))
    
    fig.add_trace(go.Surface(x=x0, y=y0, z=z0, surfacecolor=0*(x**2 + y**2 + z**2)))
    
    fig.show(renderer="browser")
        
    
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x0, y0, z0, color='w')
    for C in Circs:
        
        x, y, z = C.StereographicProjection()
        
        ax.plot3D(x, y, z, 'maroon')
    
    plt.show()





    
    
class geodesic:
    
    def __init__(self, r, x, y, z):
        self.r = r;
        self.x = x;
        self.y = y;
        self.z = z;
        
    def overlapping(self, C, tol = 1e-4):
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return d < self.r + C.r - tol;
        
    def tangent(self, C, tol = 1e-4):
        R = sqrt(self.x**2 + self.y**2 + self.z**2); # Radii of sphere
        
        
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return abs(d - (self.r + C.r)) <= tol;
    
    
    
    
    
    
    
    
    