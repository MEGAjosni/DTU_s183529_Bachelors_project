'''
#############################################
##### >>>>> Define circle objects <<<<< #####
#############################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

from compute_geodesic_circle import geodesicCircle
from polygon_intersect import intersection
import numpy as np

class circle:

    def __init__(self, P, r, ODEsys, G):
        '''
        Description
        -----------
            Constructer for circle class.

        Parameters
        ----------
        P : list
            Center coordinates.
        r : float
            Radius.
        ODEsys : function
            Object geodesic equation.
        G : function
            Metric tensor.

        Returns
        -------
        None.

        '''
        
        # Set field values
        self.P = np.array(P);
        self.r = r;
        self.coords = geodesicCircle(P, r, ODEsys, G); # <-- Numeric approximation
    
    def overlapping(self, C):
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
        
        inter = intersection(self.coords, C.coords)
        return len(inter) != 0
    
    
    def intersection(self, C):
        '''
        Description
        -----------
            Method finding intersection points between circle objects.

        Parameters
        ----------
        C : circle
            Another circle.

        Returns
        -------
        np.array
            Array of intersection points.

        '''
        
        return intersection(self.coords, C.coords)
        
    
    def tangent(self, C, ODEsys, G, tol = 0.001):
        '''
        Description
        -----------
            Method checking if object is tangent with another.

        Parameters
        ----------
        C : circle
            Another circle.
        ODEsys : function
            Object geodesic equation.
        G : function
            Metric tensor.
        tol : float
            Numeric tolerence for tangency.

        Returns
        -------
        boolean
            True if self and C are tangent.
            
        '''
        
        C1 = circle(self.P, self.r+tol, ODEsys, G)
        C2 = circle(C.P, C.r+tol, ODEsys, G)
        C3 = circle(self.P, self.r-tol, ODEsys, G)
        C4 = circle(C.P, C.r-tol, ODEsys, G)
        
        return C1.overlapping(C2) and not C3.overlapping(C4)

def tangentPairs(Circs, ODEsys, G):
    '''
    Description
    -----------
        Function finding finding tangent geodesic circle pairs from list of circles.

    Parameters
    ----------
    Circs : list
        List of circle objects.
    ODEsys : function
        Object geodesic equation.
    G : function
        Metric tensor.

    Returns
    -------
    CTaC : list
        ('C'ircle 'Ta'ngent 'C'ircle) List of tangent circle pairs.

    '''
    
    CTaC = [];
    for i in range(len(Circs)):
        for j in range(i+1, len(Circs)):
            if Circs[i].tangent(Circs[j], ODEsys, G):
                CTaC.append([i, j])
    if len(CTaC) == 1:
        print("Warning! No tangent pairs where found.")
    return CTaC