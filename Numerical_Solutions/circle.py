from compute_geodesic_circle import geodesicCircle
from polygon_intersect import intersection

class circle:
    
    def __init__(self, P, r, ODEsys, G):
        self.P = P;
        self.r = r;
        self.coords = geodesicCircle(P, r, ODEsys, G);
    
    def overlapping(self, C):
        '''

        Parameters
        ----------
        C : Circle
            Other circle.

        Returns
        -------
        Bool
            If circles are intersecting.

        '''
        
        inter = intersection(self.coords, C.coords)
        
        return len(inter) != 0
    
    def intersection(self, C):
        return intersection(self.coords, C.coords)
        
    def tangent(self, C, ODEsys, G, tol = 0.001):
        
        C1 = circle(self.P, self.r+tol, ODEsys, G)
        C2 = circle(C.P, C.r+tol, ODEsys, G)
        C3 = circle(self.P, self.r-tol, ODEsys, G)
        C4 = circle(C.P, C.r-tol, ODEsys, G)
        
        return C1.overlapping(C2) and not C3.overlapping(C4)

def tangentPairs(Circs, ODEsys, G):
    CTaC = [];
    for i in range(len(Circs)):
        for j in range(i+1, len(Circs)):
            if Circs[i].tangent(Circs[j], ODEsys, G):
                CTaC.append([i, j])
    return CTaC