import numpy as np
from matplotlib import pyplot as plt  
import time 
#Question 1
### Number of particles will be 10
Npart = 10
### create an array 'm' and 'v' to store the masses and velocities of the 10 particles... 
### initially, each entry in 'm' and 'v' will be zero, and we will have to assign values later
m = np.zeros(Npart)
v = np.zeros(Npart)
for i in range(0,Npart):
    m[i] = 1.0
    v[i] = 2.5
### Now that values have been assigned, print to confirm they are what you expect
print("Printing array of masses: ",m)
print("Printing array of velocities: ",v)
T = 1/2 * m * v**2
### confirm that T is indeed an array with an entry for the kinetic energy of each particle
print(T)
### initialize a sum variable to zero
T_tot_loop = 0.
### loop over elements of the T array and 
### compute the sum 
for i in range(0,Npart):
    ### add elements to the sum variable
    T_tot_loop = T_tot_loop + T[i]
    
### compute the sum using np.sum instead
T_tot_sum = np.sum(T)
### print both sums to confirm both methods give the same answer
print("Result from loop is ",T_tot_loop)
print("Result from numpy sum is ",T_tot_sum)
N_array = [3, 6, 9, 12, 15 ]
T_array = [6.25, 12.5, 18.75, 25.0, 31.25  ]      
plt.plot( N_array, T_array, 'red')
plt.show()

#Question 2
Npart = 10 
### create 1-D arrays of length Npart for q... assign each particle charge of 1 natural unit
q = np.ones(Npart)
### create a 1-D array of length Npart for x... use np.linspace to automatically
### assign values since we want the particles evenly spaced.
x = np.linspace(0,(Npart-1)*0.2,Npart)
### create a 2-D array that is Npart x Npart for the separations between particle pairs
r = np.zeros((Npart,Npart))
### compute all separations using two nested for-loops to access the positions of each particle
for i in range(0,Npart):
    for j in range(0,Npart):
        r[i][j] = np.sqrt( (x[i]-x[j])**2 )
### now print all arrays 
print("Printing array of charges ",q)
print("Printing array of charges ",x)
print("Printing array of charges \n",r)
### function to compute potential energy given an array of separations and an array of charges
def Potential(sep_array, charge_array):
    ### presumably the number of particles is equal to the length
    ### of the array of charges
    N = len(charge_array)
    
    ### initialize the potential energy to zer
    Pot = 0.
    ### nested loop
    for i in range(0,N):
        for j in range(0,N):
            ### do not calculate potential of particle with itself!
            if (i!=j):
                Pot = Pot + charge_array[i]*charge_array[j]/sep_array[i][j]
    return Pot
### Compute total potential energy and store it as the variable V_tot
V_tot = Potential(r, q)
### print it to see what it is!
print(V_tot)
N_array = (3, 6, 9, 12, 15)
V_array = (10.00, 43.33, 86.99, 137.43, 192.90 )
plt.plot( N_array, V_array, 'purple')
plt.show()

#Question #3
N_array = [1, 2, 3, 4, 5]
T_array = [3.125, 6.25, 9.375,  12.5, 15.625 ]      
V_array = (10.00, 43.33, 86.99, 137.43, 192.90 )
start = time.time()
x = N_array
y = start
y = T_array 
y1 = V_array
plt.plot(x, y, 'orange', x, y1, 'blue')
plt.plot(x, y, 'red')
plt.show()
end = time.time()
how_long = end - start 
print("Total time to run in seconds is: ", how_long)