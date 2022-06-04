from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import xlrd



# choose what workout to look at
WorkoutNumber = input('''What rep length (in minutes) would you like to make a plot of? 
                      This will include rep lengths close to this value (if 3, then will include 3.3).
                      Enter 6, 3, or 1:''')

# set directory
total_data = pd.read_excel('LactateLog.xlsx', 'Analysis')
#data = total_data.loc[total_data['Workout'] == int(WorkoutNumber)]
data = total_data[(total_data['Workout'] >= int(WorkoutNumber)) & (total_data['Workout'] < int(WorkoutNumber)+1)]

# visual data:
print(data)

# converting column data in numpy array
Date = np.array(data['Date'])[:, None]
Workout = np.array(data['Workout'])[:, None]
AvgSpeed = np.array(data['AvgSpeed'])[:, None]
AvgPower = np.array(data['AvgPower'])[:, None]
AvgLactate = np.array(data['AvgLactate'])[:, None]



# first plot
fig, ax1 = plt.subplots()

plot1color = 'purple'
plt.xlabel('Date')
ax1.set_ylabel('Average Power (W)', color = plot1color)
ax1.plot(Date, AvgPower, color = plot1color, label = 'Avg Power', linewidth=3)
ax1.tick_params(axis = 'y', labelcolor = plot1color)


# twin plot
ax2 = ax1.twinx()

plot2color = 'red'
ax2.set_ylabel('Average Lactate', color = plot2color)
ax2.plot(Date, AvgLactate, color = plot2color, label = 'Avg Lactate', linewidth=3)
ax2.tick_params(axis = 'y', labelcolor = plot2color)


#plot title
plt.title('Average Power vs Lactate for ' + WorkoutNumber + 'min reps')
#show plot
plt.show()
