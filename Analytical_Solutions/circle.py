'''
#############################################
##### >>>>> Define circle objects <<<<< #####
#############################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

from math import sqrt, pi
import matplotlib.pyplot as plt
import numpy as np


class circle:
    
    
    def __init__(self, r, x, y):
        '''
        Description
        -----------
            Constructer for circle class.

        Parameters
        ----------
        r : float
            Radius.
        x : float
            x-coordinate.
        y : float
            y-coordinate.

        Returns
        -------
        None.

        '''
            
        self.x = x;
        self.y = y;
        self.r = r;

    def overlapping(self, C, tol=1e-4):
        '''
        Description
        -----------
            Method checking if object overlaps with another.

        Parameters
        ----------
        C : circle
            Another circle.

        Returns
        -------
        boolean
            True if self and C overlap.

        '''
        
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return d < self.r + C.r - tol;
        
    def tangent(self, C, tol=1e-4):
        d = sqrt((self.x - C.x)**2 + (self.y - C.y)**2);
        return abs(d - (self.r + C.r)) <= tol or abs(d - abs(self.r - C.r)) <= tol;

    def intersection(self, C, t=0, tol=1e-4):
        '''
        Description
        -----------
            Method finding intersection points between circle objects.

        Parameters
        ----------
        C : circle
            Another circle.
        
        t : float
            Radius increase.
        tol : float, optional
            Numerical error tolerance. The default is 1e-4.

        Returns
        -------
        list
            List of intersection points.

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
            print('Warning! Circles do not intersect.')
            return [None, None]
            
        p1 = A - B;
        p2 = A + B;
        
        return [p1, p2]
        

    def show(self):
        '''
        Description
        -----------
            Plots itself

        Returns
        -------
        plt object
            Plot of circle.

        '''
        return plt.Circle((self.x, self.y), self.r, fill=False, lw=0.2);
    
    def StereographicProjection(self):
        '''
        Description
        -----------
            Project circle onto unit sphere through the stereographic projection.

        Returns
        -------
        np.array
            Cartesian coordinates of circle on sphere.

        '''
        
        theta = np.linspace(0, 2*pi, 100, endpoint=True)
        
        X = self.x + np.cos(theta)*self.r
        Y = self.y + np.sin(theta)*self.r     

        x = 2*X / (1 + X**2 + Y**2)
        y = 2*Y / (1 + X**2 + Y**2)
        z = (-1 + X**2 + Y**2) / (1 + X**2 + Y**2)

        return x, y, z


    def describe(self):
        '''
        Description
        -----------
            Make a circle present it fields.

        Returns
        -------
        None

        '''
        print('r = {}, center = [{}, {}].'.format(self.r, self.x, self.y));
        return

def tangentPairs(Circs):
    '''
    Description
    -----------
        Function finding finding tangent circle pairs from list of circles.

    Parameters
    ----------
    Circs : list
        List of circle objects.

    Returns
    -------
    CTaC : list
        ('C'ircle 'Ta'ngent 'C'ircle) List of tangent circle pairs.

    '''
    
    CTaC = [];
    for i in range(len(Circs)):
        for j in range(i+1, len(Circs)):
            if Circs[i].tangent(Circs[j]):
                CTaC.append([i, j])
    return CTaC
    

    
    
    
    
    
    
    
    