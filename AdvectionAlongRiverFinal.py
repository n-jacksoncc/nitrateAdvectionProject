import numpy as np
import matplotlib.pyplot as plt

'set up initial conditions'
# we are asked to model with a dx of 20
dx = 20 # meters
# we are also told to model this across a 5 km distance
x = np.arange(0, 5001, dx)  #meters


#velocity
# we are told that the wind velocity is modeled within a sin function of specified parameters
u = np.sin(x/100+600)+5

nodes = len(x)

# the concentration of the silver iodide is 10^-7 kg/m^3 and is pumped only in the nodes between 40 and 100 meters
C = np.zeros(nodes)
C[(x>=40) & (x<=100)] = 10**-7


# plot the initial condtions
plt.figure()
plt.plot(x,u)
plt.xlabel("Distance (m)")
plt.ylabel("Velocity (m/s)")
plt.title("Wind Velocity Over Time -- Question 1")


' set up the A matrix'

# u is not constant anymore
# courant must be less than one
dt = dx/np.max(u) # seconds

courant = dt*u/dx

A = np.zeros((nodes, nodes))


for i in range(1,nodes-1):
    if i >0:
        A[i,i] = 1 - courant[i]
        A[i, i-1]  = courant[i]

seconds = 0
endtime = 10*60

fig, ax = plt.subplots(1,1)
ax.plot(x,C, '--k', label = "initial")


' dot product'
while seconds <= endtime:
    C_new = np.dot(A, C)
    C[:] = C_new*1
    seconds += dt
    
    
# plot the steady state conditions
ax.plot(x, C, label = "10 minutes") 
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Concentration (kg/m^3)")
ax.set_title("Steady state conditions")  
plt.legend()
plt.show()