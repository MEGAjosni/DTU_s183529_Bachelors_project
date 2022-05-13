# -*- coding: utf-8 -*-
"""
@author: jonas
"""

from circle import circle
from math import sqrt, inf
import numpy as np

def SimplePacking(Circs, CTaC, InDomain, t_min=1, t_max=5, tol=1e-4, max_it=inf):
    '''
    ##################################################
    ############ >>>>> Run Algorithm <<<<< ###########
    ##################################################
    '''
    
    it = 0;
    while CTaC and it < max_it:
        print(len(CTaC))
        it += 1
        
        # Get next pair of tangent circles
        # i = np.random.randint(len(CTaC));
        # idx = CTaC.pop(i)
        
        idx = CTaC.pop(0)
        
        C1 = Circs[idx[0]];
        C2 = Circs[idx[1]];

        # Grow circles
        for k in range(2):
            
            x1, x2 = C1.x, C2.x
            
            if not C1.Usualtangent(C2):
                if x1 > x2:
                    x2 += 2*np.pi
                else:
                    x1 += 2*np.pi
            
            R = sqrt((x1 - x2)**2 + (C1.y - C2.y)**2)
            
            def x(t):
                
                
                A = 1/2*(x1 + x2) + ((C1.r + t)**2 - (C2.r + t)**2)/(2*R**2)*(x2 - x1)
                B = 1/2*sqrt(2*((C1.r + t)**2 + (C2.r + t)**2)/R**2 - ((C1.r + t)**2 - (C2.r + t)**2)**2/R**4 - 1)*(C2.y - C1.y)
                return (A + (-1)**k * B) % (2*np.pi)
            
            def y(t):
                A = 1/2*(C1.y + C2.y) + ((C1.r + t)**2 - (C2.r + t)**2)/(2*R**2)*(C2.y - C1.y)
                B = 1/2*sqrt(2*((C1.r + t)**2 + (C2.r + t)**2)/R**2 - ((C1.r + t)**2 - (C2.r + t)**2)**2/R**4 - 1)*(x1 - x2)
                return A + (-1)**k * B
                
            
            # Check if largest will fit
            Cp = circle(t_max, x(t_max), y(t_max));
            if InDomain(Cp) and all([not Cp.overlapping(C, tol=tol) for C in Circs]):
                # Add circle and find tangent pairs
                N = len(Circs)
                for i, C in enumerate(Circs):
                    if Cp.tangent(C, tol=tol):
                        CTaC.append([i, N])
                
                Circs.append(Cp)
            
            else:
                # Check if smallest size will fit
                Cp = circle(t_min, x(t_min), y(t_min));
                valid = InDomain(Cp) and all([not Cp.overlapping(C, tol=tol) for C in Circs if C not in [C1, C2]])

                # Converge circle
                if valid:
                    
                    r_lower = t_min;
                    r_upper = t_max;
                    converged = False
                    
                    while not converged:
                        
                        r_mid = (r_lower + r_upper) / 2
                        Cp = circle(r_mid, x(r_mid), y(r_mid));
                    
                        if InDomain(Cp) and all([not Cp.overlapping(C, tol=tol) for C in Circs if C not in [C1, C2]]):
                            r_lower = r_mid
                        else:
                            r_upper = r_mid
                        
                        if abs(r_lower - r_upper) <= tol:
                            converged = True
                    
                    # Add circle and find new tangent pairs
                    N = len(Circs)
                    for i, C in enumerate(Circs):
                        if Cp.tangent(C, tol=tol):
                            CTaC.append([i, N])
                    CTaC.append(idx)
                    Circs.append(Cp)
    
                
    return


def InitialTangent(Circs):
    CTaC = [];
    for i in range(len(Circs)):
        for j in range(i+1, len(Circs)):
            if Circs[i].tangent(Circs[j]):
                CTaC.append([i, j])
    return CTaC