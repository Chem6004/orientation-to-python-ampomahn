# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:43 2019

@author: ampomahn
"""

#print("Hello Word!")
# m = 1.0 m can represent an array of numbers 
# v = 5.0 v will list arrays of particles
# T represents addition of alll times noted 
###different ways to write equations for (K.E)
#T1 = 0.5*m*v**2
#T2 = 1/2 * m * v * v
#T3 = 0.5 * m * v * v
#T4 = m*v**2/2
#print( T1, T2, T3, T4)
#in order to find P.E must know position and time, requires more than 1 particle
#m1 = 1.0 
#v1 = 5.0
#q1 = 1.0
#x1 = 0.0


###  variable for particle 2
#m2 = 1.0
#v2 = 2.5
#q2 = 1.0
#x2 = 0.5
import numpy as np
Npart = 10
## create empty lists for each quantitiy 
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart)
T = np.zeros(Npart)
## print the array of zeros for m
print(m)
# i represents increment by 1, **statrting from 0** to structure loop
for i in range(0,Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5 * i #for position 
    v[i] = 0.2 * i
    
    ### now that m & v have been found for the ith particle, I can calcute K.e for ith particle
    T[i] = 0.5 * m[i] * v[i]**2
    
print(T)    
    
print(m) 
print(q)
print(x)
print(v)    
    

###  variable for pair particles (positions of particles)
#r12 = np.sqrt((x1-x2)**2)
#V12 =  q1*q2/r12
## q1*q2 for P.E q is charge
#print(" separation is ",r12)
#print("Potential energy is ",V12)