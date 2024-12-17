import numpy as np
import matplotlib.pyplot as plt
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
dx = 1000 # meters

# the distance from USGS site #07091200 to the border between Colorado and Kansas
x = np.arange(0, 363000, dx)  #meters
nodes = len(x)

#velocity in km/s
u = np.zeros(nodes)
u[(x<60433)] = ws['E2'].value #site number 7091200
u[(60433<=x) & (x<133863)] = ws['E3'].value  #site number 7094500
u[(133863<=x) & (x<150633)] = ws['E4'].value  # site number 7099973
u[(150633<=x) & (x<253793)] =  ws['E5'].value  # site number 7109500
u[(253793<=x) & (x<279563)] =  ws['E6'].value  # site number 71224000
u[(279563<=x) & (x<310262)] =  ws['E7'].value  # site number 7130500
u[(310262<=x) & (x<336549)] =  ws['E8'].value  # site number 7130500
u[(336549<=x) & (x<354592)] =  ws['E9'].value  # site number 7134180
u[(354592<x)] = ws['E10'].value  # site number 7135500


# the concentration of nitrate that is released 60.433 km from the start site
C = np.zeros(nodes)
C[(x<=30216)] = 100 # mg/L



# plot the initial condtions
plt.figure()
plt.plot(x,u)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Distance (m)")
plt.ylabel("Velocity (m/s)")
plt.title("Average Spring and Summer Arkansas River Velocity Through Space")
plt.tight_layout()


'SET UP THE A MATRIX'

# u is not constant anymore
# courant must be less than one
dt = dx/np.max(u) # seconds

courant = dt*u/dx

A = np.zeros((nodes, nodes))

for i in range(1,nodes-1):
    if i > 0:
        A[i,i]= 1-courant[i]
        A[i,i-1]= courant[i]


seconds = 0
endtime = 60*60*24  #1 day

fig, ax = plt.subplots(1,1)
ax.plot(x,C, '--k', label = "initial")


' DOT PRODUCT'
while seconds <= endtime:
    C_new = np.dot(A, C)
    C[:] = C_new*1
    seconds += dt
   
    
'PLOT THE FINAL CONDITIONS'

# note that this code does not currently display the final concentration graph correctly
ax.plot(x, C, label = "1 day") 
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Concentration (mg/L)")
ax.set_title("Nitrate Advection in Over One Day Through the Arkansas River") 
plt.xticks(rotation=45, ha='right')
fig.tight_layout()
plt.legend()
plt.show()