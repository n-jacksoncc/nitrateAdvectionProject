# *Simple 1D Nitrate Advection Model*

## Model Purpose
This simple numerical model demonstrates the theoretical 1 dimensional advection of nitrate deposits through the Arkansas River. This model assumes that nitrate deposition occurs exclusively at one sector in the river, and that it advects without changes to its concentration (no supply or degradation).The model produces a plot of the advection of nitrate through the Arkansas River over one day, as well as the velocity of river through space. This model can be utilized to replicate the advection of any mineral or ion in any river, as long as the appropriate input parameters are adjusted.

## Date Imports
This model imports one excel datasheet that contains data obtained from USGS datasites. In particular, USGS collected monthly average discharge rates for the months of April - September for nine respective data collection sites were averaged for an average spring discharge rate for each site. Because the USGS did not publish pure velocities or cross-sectional areas, the gauge heights for each month were averaged per site, and were multiplied by GoogleEarth measured river widths at each site. The average discharge rate for each site was divided by the approximate cross-sectional area to obtain a velocity measurement in ft/s for each site. This data was converted to m/s for continuity with the rest of the model. 

The model assumes that site one is the zeroth point spatially on the graph, and thus, the velocity measurement at that point is assumed to be constant within the river until the next data collection site. The distances between the data collection sites were measured via GoogleEarth. The velocity measurements are input into an array of velocities wherein each x value is the distance from the start (in meters) at which that velocity occurs. The cell in the excel spreadsheet where the data for that specific site is stored is referenced in velocity variable assignment (Ex: u[(x<60444)] = ws['E3'].value means that from distances of 0-60444 meters, the velocity can be found in cell E3)

To utilize the model for a different river, ensure that the velocity assignment statements are unique to the data collected for that specific river. Update the index of the u and the cell of the excel spreadsheet referenced as needed. 

## Running the Model
Change the ws filepath as needed to ensure that the model can locate the velocity_data.xlsx spreadsheet on your device. Change the input parameters as specified in the comments at the top of the .py file if you run the model for a different river. 

## Model Challenges
Note that there is some false diffusion present in this model due to the variable velocities throughout the river. The dx and dt values present currently were optimized to minimize false diffusion by ensuring a courant number as close to 1 as possible. When utilizing this model, adjust dx and dt as needed for the unique data relevant to the problem. 

## Collection Site Visual
<img width="1157" alt="Screen Shot 2024-12-17 at 11 17 19 PM" src="https://github.com/user-attachments/assets/2bc1e65c-cc68-48e1-8a7f-26bfa95d4457" />

