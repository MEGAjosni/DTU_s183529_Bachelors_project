# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:13:51 2022

@author: jonas
"""

from circle import circle

def OpenDomain(C):
    return True

def InBox(C):
    """
    Desciption
    ----------
    Determining if a point lies within a n-dimensional box.

    Parameters
    ----------
    x : list
        Point to be checked.
    x0 : list
        Lower initial point.
    L : list
        Box side lengths.

    Returns
    -------
    bool
        True if x is in domain, and false if not.

    """
    
    x_range = [-1, 1];
    y_range = [-1, 1];
    
    return C.x-C.r >= x_range[0] and C.x+C.r <= x_range[1] and C.y-C.r >= y_range[0] and C.y+C.r <= y_range[1] 


def InBall(C):
    """
    Desciption
    ----------
    Determining if an n-dimensional ball lies within an n-dimensional ball.

    Parameters
    ----------
    x : list
        Ball center.
    r : scalar
        Ball radius
    x0 : list
        Domain ball center.
    L : list
        Domain ball radius.

    Returns
    -------
    bool
        True if ball is in domain, and false if not.

    """
    
    domainC = circle(1, 0, 0);
    
    from numpy.linalg import norm
    
    return norm([domainC.x-C.x, domainC.y-C.y]) <= domainC.r-C.r


def InBallSphere(C):
    """
    Desciption
    ----------
    Determining if an n-dimensional ball lies within an n-dimensional ball.

    Parameters
    ----------
    x : list
        Ball center.
    r : scalar
        Ball radius
    x0 : list
        Domain ball center.
    L : list
        Domain ball radius.

    Returns
    -------
    bool
        True if ball is in domain, and false if not.

    """
    
    domainC = circle(7.5, 0, 0);
    
    from numpy.linalg import norm
    
    return norm([domainC.x-C.x, domainC.y-C.y]) <= domainC.r-C.r
    
def InEllipsoid(x, x0, Ha):
    """
    Desciption
    ----------
    Determining if a point lies within a n-dimensional ellipsoid.

    Parameters
    ----------
    x : list
        Point to be checked.
    x0 : list
        Elipsoid center.
    L : list
        Half axes.

    Returns
    -------
    bool
        True if x is in domain, and false if not.

    """
    
    import numpy as np
    
    x = np.array(x);
    x0 = np.array(x0);
    Ha = np.array(Ha)
    
    if np.sum(np.divide((x-x0)**2, Ha**2)) <= 1:
        return True
    else:
        return False


def InBinary(C):
    
    import matplotlib.pyplot as plt
    import numpy as np

    img = plt.imread('graphix/dtu.png')[:, :, 0]
    img = np.round(img)
    img = np.flip(img, axis=0)
    
    m, n = img.shape
    
    if C.x - C.r < 0 or C.x + C.r > n or C.y - C.r < 0 or C.y + C.r > m:
        return False
    
    for i in range(max(0, int(C.x - C.r)), min(int(C.x + C.r) + 1, n)):
        for j in range(max(0, int(C.y - C.r)), min(int(C.y + C.r) + 1, m)):
            if img[j, i] == 0 and not (C.x+C.r <= j and C.x-C.r <= j+1 and C.y+C.r >= i and C.y-C.r <= i+1):
                return False
    
    return True
    
    
    
    






























