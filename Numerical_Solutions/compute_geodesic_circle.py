from numpy import pi, cos, sin, sqrt, linspace, array

'''
################################################
##### >>>>> Compute geodesic circles <<<<< #####
################################################
'''
def geodesicCircle(P, r, ODEsys, G, N=100):
    
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