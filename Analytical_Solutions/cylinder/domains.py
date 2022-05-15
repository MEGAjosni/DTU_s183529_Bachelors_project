# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:13:51 2022

@author: jonas
"""

from numpy import pi

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
    
    y_range = [0, pi];
    
    return C.y-C.r >= y_range[0] and C.y+C.r <= y_range[1] 






























