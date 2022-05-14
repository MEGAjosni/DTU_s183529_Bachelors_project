# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 13:30:27 2022

@author: jonas
"""

from math import sqrt, cos, sin, pi
import matplotlib.pyplot as plt
import numpy as np
import tikzplotlib


class circle:
    
    def __init__(self, r, x, y):
        self.x = x;
        self.y = y;
        self.r = r;

    def overlapping(self, C, tol=1e-4):
        deltaX = min(abs(self.x - C.x), 2*np.pi - abs(self.x - C.x))
        deltaY = abs(self.y - C.y)
        d = sqrt(deltaX**2 + deltaY**2);
        return d < self.r + C.r - tol;
        
    def tangent(self, C, tol=1e-4):
        deltaX = min(abs(self.x - C.x), 2*np.pi - abs(self.x - C.x))
        deltaY = abs(self.y - C.y)
        d = sqrt(deltaX**2 + deltaY**2);
        return abs(d - (self.r + C.r)) <= tol or abs(d - abs(self.r - C.r)) <= tol;
    
    def Usualtangent(self, C, tol=1e-4):
        deltaX = abs(self.x - C.x)
        deltaY = abs(self.y - C.y)
        d = sqrt(deltaX**2 + deltaY**2);
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

    def describe(self):
        print("r = {}, center = [{}, {}].".format(self.r, self.x, self.y));


def ShowCircles(Circs, fileName=False):

    import matplotlib.pyplot as plt
    
    # Lets draw a circle
    fig, ax = plt.subplots();
    ax.set_aspect(1);
    
    # Display circles
    for i, C in enumerate(Circs):
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
        plt.savefig('.svg', format='svg')
        tikzplotlib.save('frontimg.tex')
    plt.show();
    
    
def ShowCirclesOnCylinder(Circs):
    
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    fig = make_subplots()
    
    fig.update_layout(scene_aspectmode='manual',
                  scene_aspectratio=dict(x=1, y=1, z=3))
    
    def r(phi, z):
        return np.cos(phi), np.sin(phi), z
    
    for C in Circs:
        
        theta = np.linspace(0, 2*pi, 100, endpoint=True)
    
        phi = C.x + C.r*np.cos(theta)
        z = C.y + C.r*np.sin(theta)
    
        x, y, z = r(phi, z)
        
        fig.add_trace(go.Scatter3d(x=x, y=y,z=z, mode='lines', line_color='black'))
    
    
    # Plot cylinder
    def cylinder(r, h, a=0, nt=100, nv =50):

        theta = np.linspace(0, 2*np.pi, nt)
        v = np.linspace(a, a+h, nv )
        theta, v = np.meshgrid(theta, v)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        z = v
        return x, y, z
    
    
    x, y, z = cylinder(1, 2*np.pi)
    
    fig.add_trace(go.Surface(x=x, y=y, z=z, showscale=False))

    fig.show(renderer="browser")

