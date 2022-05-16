'''
Written by
----------
    Author:     Jonas Søeborg Nielsen
    Date:       May 16, 2022
'''

from circle import circle

def OpenDomain(C):
    return True

def InBox(C):
    '''
    Description
    ----------
        Determining if a circle lies within a rectangle.

    Returns
    -------
    bool
        True if x is in domain, and false if not.

    '''
    
    x_range = [-1, 1];
    y_range = [-1, 1];
    
    return C.x-C.r >= x_range[0] and C.x+C.r <= x_range[1] and C.y-C.r >= y_range[0] and C.y+C.r <= y_range[1] 


def InBall(C):
    '''
    Description
    ----------
        Determining if a circle lies within a circular domain.

    Returns
    -------
    bool
        True if ball is in domain, and false if not.

    '''
    
    domainC = circle(1, 0, 0);
    
    from numpy.linalg import norm
    
    return norm([domainC.x-C.x, domainC.y-C.y]) <= domainC.r-C.r


def InBallSphere(C):
    '''
    Description
    ----------
        Determining if a circle lies within a circular domain.

    Returns
    -------
    bool
        True if ball is in domain, and false if not.

    '''
    
    domainC = circle(7.5, 0, 0);
    
    from numpy.linalg import norm
    
    return norm([domainC.x-C.x, domainC.y-C.y]) <= domainC.r-C.r


def InBinary(C):
    '''
    Description
    ----------
        Determining if a circle lies within a domain given by a binary image.

    Returns
    -------
    bool
        True if circle is in domain, and false if not.

    '''
    
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
    
    
    
    






























