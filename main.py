# importing library and having it use the agg backend
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# a try that reads the file with a catch that will print out if the file is not found
try:
    with open('./gasData.dat', 'r', newline = '\r\n') as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found")
    exit()
# initializing the x and y values
x = []
y = []

# for loop that will loop through the .dat file and assigning the x and y values to the corresponding variable
for line in data:
    try:
        i = line.strip().split(',')
        x.append(i[0])
        y.append(float(i[1]))
    # catch that will print if a variable is not read properly
    except ValueError:
        print(f"Skipping line: {line}")
        continue

# sets the x-axis to show the month of april every 3 years, 36 months, so that the x-axis is not so cluttered
xTicks = x[::36]

# sets the assigns the xAxis and yAxis variable to the corresponding axes
xAxis, yAxis = plt.subplots()

# this gives more space to the bottom of the graph so the x-axis is not cut off
xAxis.subplots_adjust(bottom = 0.2)

# plots the x and y variables that we have to the graph
plt.plot(x, y)
# rotates the x-axis labels 90 degrees so it is easier to read.
plt.xticks(xTicks, rotation = 90)
# gives the x-axis a title
plt.xlabel('Date (Year)')
# gives the y-axis a title
plt.ylabel('Gas Prices (Dollar Per Gallon)')
# gives the graph a title
plt.title('Gas Prices for the Past 30 Years')
# saves the graph as a png
plt.savefig('gasPlot.png')
