# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 06:34:21 2015

@author: manmadan03
"""
import numpy as np

def extrema(x, movingwindowsize = 1, movingwindow = False):
    xmax = xmin = imax = imin = np.array([])
    #Check if x is an array or ndarray
    if x.ndim != 1:
        raise TypeError('Input is not an 1D array')
    nt = len(x)
    #check for nans

    inan = np.array(np.where(np.isnan(x))).flatten()
    indx = np.arange(0,nt)


    if len(inan) > 0:
        x = np.delete(x,inan)
        indx = np.delete(indx,inan)
        nt = len(x)

    #diff
    print 'Finding diff'
    dx = np.diff(x)

    print 'Finding lines'
    print dx
    #check for horizontal lines
#    if len(dx) > 0:
#        return

    print 'Finding flat peaks'
    #flat peaks
    a = np.array(np.where(dx != 0)).flatten()
    lm = np.array(np.where(np.diff(a) != 1)) + 1
    d = a[lm] - a[lm - 1]
    a[lm] = a[lm] - np.floor(d / 2)
    a = np.append(a, np.array([nt - 1]))
    #peaks?
    xa = x[a]
    b = (np.diff(xa) > 0)
    xb = np.diff(b + 0)
    imax = np.array(np.where(xb == -1)) + 1
    imin = np.array(np.where(xb == +1)) + 1
    imax = a[imax]
    imin = a[imin]
    imax = imax.flatten()
    imin = imin.flatten()
    nmaxi = len(imax)
    nmini = len(imin)
    if nmaxi == 0 and nmini == 0:
        if x[0] > x[nt]:
            xmax = x[0]
            imax = indx[0]
            xmin = x[nt]
            imin = indx[nt]
        elif x[0] < x[nt]:
            xmax = x[nt]
            imax = indx[nt]
            xmin = x[0]
            imin = indx[0]
        return [xmax, xmin, imax, imin]

    #Maximum or minimum at ends
    if nmaxi == 0:
        imax[:2] = [1, nt]
    elif nmini == 0:
        imin[:2] = [1, nt]
    else:
        if imax[0] < imin[0]:
            imin = np.append(np.array([1]), imin)
#            imin[1 : nmini] = imin
#            imin[0] = 1
        else:
            imax = np.append(np.array([1]), imax)
#            imax[1: nmaxi] = imax
#            imax[0] = 1
        if imax[-1] > imin[-1]:
            imin = np.append(imin, np.array([nt - 1]))
#            imin[len(imin) + 1] = nt
        else:
            imax = np.append(imax, np.array([nt - 1]))
#            imax[len(imax) + 1] = nt

    xmax = x[imax]
    xmin = x[imin]

    #nan's
    if len(inan) > 0:
        imax = indx[imax]
        imin = indx[imin]

    #same size as x
    imax = np.reshape(imax, np.shape(xmax))
    imin = np.reshape(imin, np.shape(xmin))

    #descending order
    inmax = np.argsort(-xmax)
    xmax = xmax[inmax]
    imax = imax[inmax]
    inmin = np.argsort(xmin)
    xmin = np.sort(xmin)
    imin = imin[inmin]

    return [xmax, xmin, imax, imin]
