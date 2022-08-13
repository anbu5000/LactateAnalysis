from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import xlrd



# choose what workout to look at
WorkoutNumber = input('''What rep length (in minutes) would you like to make a plot of? 
                      Enter 6, 3, or 1:''')
6

# set directory
total_data = pd.read_excel('LactateLog.xlsx', 'Analysis')
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
ax1.set_ylabel('Watts', color = plot1color)
ax1.plot(Date, AvgPower, color = plot1color, label = 'Average Power', linewidth=3)
ax1.tick_params(axis = 'y', labelcolor = plot1color)


# twin plot
ax2 = ax1.twinx()

plot2color = 'red'
ax2.set_ylabel('mmol/L', color = plot2color)
ax2.plot(Date, AvgLactate, color = plot2color, label = 'Average Lactate', linewidth=3)
ax2.tick_params(axis = 'y', labelcolor = plot2color)
ax2.axhline(3, color = 'red', linestyle = 'dashed')
ax2.axhline(2, color = 'red', linestyle = 'dashed')

#plot title and legend
plt.title('Average Power vs Lactate for ' + WorkoutNumber + 'min reps')
fig.legend(loc = 'upper left')
#show plot
plt.show()
