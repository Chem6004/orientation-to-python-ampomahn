# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:08:39 2019

@author: ampomahn
"""

import numpy as np
import pylab
import math
from matplotlib import pyplot as plt
pi = math.pi
m = 1.0
l = 10.0

def H_ij(i,j):
    if i == j:
        ham_int = ((np.pi**2 * j**2) / (2*m*(l**2))) + ((np.sqrt(2/10)) * np.sin(j*pi*5/10))
    else:
        ham_int = np.pi**2 * j**2 / 2*m * l**2 
    return ham_int
    
H_mat = np.zeros((3,3))
for i in range(1,4):
    for j in range(1,4):
        H_mat[i-1][j-1] = H_ij(i,j)
print(H_mat)

c = np.zeros(3)

c[0] = 1
Hc = np.dot(H_mat,c)
E = np.dot(np.transpose(c),Hc)
print(E)