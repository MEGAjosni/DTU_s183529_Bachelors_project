'''
#######################################
##### >>>>> Packing routine <<<<< #####
#######################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

from numpy import pi
from surfaces import torusODEsystem, torusG
from joblib import Parallel, delayed
from circle import circle, tangentPairs
from math import inf

def packOnSurface(Circs, r_min=pi/24, r_max=pi/12, N=100, u_range=[-pi, pi], v_range=[-pi, pi], maxit=inf, ODEsys=torusODEsystem, G=torusG):
    '''
    Description
    -----------
        This routine packs geodesic circles on the surface of a given surface using an initial set of tangent circle pairs.
        The used algorithm is tangent circle pair growing.
    
    Parameters
    ----------
    Circs : list
        List of initial circles. Gets updated by routine with new circles.
    r_min : float, optional
        Lower bound on circle radius. The default is pi/24.
    r_max : float, optional
        Upper bound on circle radius. The default is pi/12.
    N : int, optional
        Number of points in approximation of geodesic circles. The default is 100.
    u_range : list, optional
        Range of the u parameter. The default is [-pi, pi].
    v_range : list, optional
        Range of the v parameter. The default is [-pi, pi].
    maxit : int, optional
        Upper limit on the number of iterations routine will run. The default is inf.
    ODEsys : function
        Object geodesic equation.
    G : function
        Metric tensor.

    Returns
    -------
    None.
    '''
    
    # Define domain function
    def InDomain(Cp):
        return min(Cp.coords[:,0]) > u_range[0] and max(Cp.coords[:,0]) < u_range[1] and min(Cp.coords[:,1]) > v_range[0] and max(Cp.coords[:,1]) < v_range[1]
    
    # Find initial tangent pairs
    CTaC = tangentPairs(Circs, ODEsys, G)
    
    it = 0
    while CTaC and it < maxit:
        print("===============")
        print("Iteration: {}".format(it))
        print("#Circs: {}".format(len(Circs)))
        print("#CTaC: {}".format(len(CTaC)))
        
        # Get tangent circles
        idx = CTaC.pop(0);
        C1 = Circs[idx[0]];
        C2 = Circs[idx[1]];
        
        for k in range(2):
            
            # Try largest
            new_centers = circle(C1.P, C1.r + r_max, ODEsys, G).intersection(circle(C2.P, C2.r + r_max, ODEsys, G))
            Cp = circle(new_centers[k], r_max, ODEsys, G)
            print(new_centers)
            
            valid = True;
            
            # Check for overlaps (use multithreading to speed up)
            g = Parallel(n_jobs=8)(delayed(Cp.overlapping)(C) for C in Circs)
            g[idx[0]], g[idx[1]] = False, False
            valid = not any(g)
            
            if not InDomain(Cp):
                valid = False;
            
            if not valid:
                # Try smallest
                new_centers = circle(C1.P, C1.r + r_min, ODEsys, G).intersection(circle(C2.P, C2.r + r_min, ODEsys, G))
                Cp = circle(new_centers[k], r_min, ODEsys, G)
                
                # Check for overlaps (use multithreading to speed up)
                g = Parallel(n_jobs=8)(delayed(Cp.overlapping)(C) for C in Circs)
                g[idx[0]], g[idx[1]] = False, False
                valid = not any(g)
                
                if not InDomain(Cp):
                    valid = False;
                    
                # Converge circle
                if valid:
                    r_lower = r_min;
                    r_upper = r_max;
                
                    for i in range(10):
                        r_mid = (r_lower + r_upper) / 2
                        new_centers = circle(C1.P, C1.r + r_mid, ODEsys, G).intersection(circle(C2.P, C2.r + r_mid, ODEsys, G))
                        Cp = circle(new_centers[k], r_mid, ODEsys, G);
                
                        # Check for overlaps (use multithreading to speed up)
                        g = Parallel(n_jobs=8)(delayed(Cp.overlapping)(C) for C in Circs)
                        g[idx[0]], g[idx[1]] = False, False
                        valid = not any(g)
                        
                        if not InDomain(Cp):
                            valid = False;
                        
                        if valid:
                            r_lower = r_mid
                        else:
                            r_upper = r_mid
                else:
                    continue

            # Add new tangent pairs
            N = len(Circs)
            for i, C in enumerate(Circs):
                if Cp.tangent(C, ODEsys, G):
                    CTaC.append([i, N])
            Circs.append(Cp)

        it += 1;
    
    return
