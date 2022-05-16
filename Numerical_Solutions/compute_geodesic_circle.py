'''
####################################################
##### >>>>> Approximate geodesic circles <<<<< #####
####################################################

Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

from numpy import pi, cos, sin, sqrt, linspace, array

def geodesicCircle(P, r, ODEsys, G, N=100):
    '''
    Description
    -----------
        Function approximating a geodesic circle.

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
    N : int, optional
        Number of points in approximation. The default is 100.

    Returns
    -------
    np.array
        Coordinates of points in geodesic circle approximation.

    '''
    
    # Import relevant packages
    from scipy.integrate import solve_ivp
    
    # Use shooting to obtain points on geodesic circle
    geodesic_circle = [];    
    for theta in linspace(0, 2*pi, N):
        # Setup normalized shoot direction
        v0 = array([cos(theta), sin(theta)]);
        norm_factor = sqrt(v0.T @ G(P) @ v0)
        v0 /= norm_factor
        
        # Shoot using solve_ivp and append solution
        y0 = [P[0], P[1], v0[0], v0[1]]
        sol = solve_ivp(ODEsys, [0, r], t_eval=[r], y0=y0)
        geodesic_circle.append(sol.y.T[0][0:2])
        
    return array(geodesic_circle)