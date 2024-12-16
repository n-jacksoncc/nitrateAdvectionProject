import numpy as np
import matplotlib.pyplot as plt
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

"""
This code is meant to numerically model the 1d advection of nitrite and nitrate through the Arkansas River. It utilizes 
available USGS data for data collection site discharge within the river and potential nitrate concentration contributors. 
This code can be adapted for other rivers. 

Input Parameters:
    wb = the file path unique to the user leading to the Excel spreadsheet with velocity values
    u = velocity values (ft/s) currently assuming that velocity values will be input in the B column in excel
    dx = the change in x between nodes (km) 
    x = the grid of distances from the start location (km)
    C = the initial concentration of nitrate (mg/L) at the initial source location
    dt = the change in time at which each calculation will be performed (s)
    endtime =  the total amount of time the model will run for (s)
  
    
Output Parameters:
    courant = the stability parameter for advection --> ensure that this value is as close to, but does not exceed 1
    two plots: river velocity over space and advection of nitrate over space initially and at the end time
"""



'SET UP INITIAL CONDITIONS' 

# set up the workbook and worksheet for loading in the data
wb = load_workbook("/Users/nadia/Downloads/NumericalModeling/Homework/finalProject/velocity_data.xlsx")
ws = wb.active

# the dx is currently set to 7 due to the variety in distances between the velocity measurements
dx = 7 # kilometers

# the distance from USGS site #07091200 to the border between Colorado and Kansas
x = np.arange(0, 363, dx)  #kilometers
nodes = len(x)

#velocity in ft/s
u = np.zeros(nodes)
u[(x<60.433)] = ws['B2'].value #site number 7091200
u[(60.433<=x) & (x<133.863)] = ws['B3'].value  #site number 7094500
u[(133.863<=x) & (x<150.633)] = ws['B4'].value  # site number 7099973
u[(150.633<=x) & (x<253.793)] =  ws['B5'].value  # site number 7109500
u[(253.793<=x) & (x<279.563)] =  ws['B6'].value  # site number 71224000
u[(279.563<=x) & (x<310.262)] =  ws['B7'].value  # site number 7130500
u[(310.262<=x) & (x<336.549)] =  ws['B8'].value  # site number 7130500
u[(336.549<=x) & (x<354.592)] =  ws['B9'].value  # site number 7134180
u[(354.592<x)] = ws['B10'].value  # site number 7135500


# the concentration of nitrate that is released 60.433 km from the start site
C = np.zeros(nodes)
C[(x<=60.433)] = 100 # mg/L


# plot the initial condtions
plt.figure()
plt.plot(x,u)
plt.xlabel("Distance (km)")
plt.ylabel("Velocity (ft/s)")
plt.title("River Velocity")


'SET UP THE A MATRIX'

# u is not constant anymore
# courant must be less than one
dt = dx/np.max(u) # seconds

courant = dt*u/dx

A = np.zeros((nodes, nodes))
for i in range(1,nodes-1):
    if i >0:
        A[i,i] = 1 - courant[i]
        A[i, i-1]  = courant[i]
        
A[0, 0] = 1
A[-1, -1] = 1

seconds = 0
endtime = 60*60*24  #one day

fig, ax = plt.subplots(1,1)
ax.plot(x,C, '--k', label = "initial")


' DOT PRODUCT'
while seconds <= endtime:
    C_new = np.dot(A, C)
    C[:] = C_new*1
    
    seconds += dt
    
    
'PLOT THE FINAL CONDITIONS'

# note that this code does not currently display the final concentration graph correctly
ax.plot(x, C, label = "1 hour") 
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Concentration (mg/L)")
ax.set_title("Steady state conditions")  
plt.legend()
plt.show()