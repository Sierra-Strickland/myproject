# importing libraries
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

try:
    with open('./gasData.dat', 'r', newline = '\r\n') as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found")
    exit()

x = []
y = []

for line in data:
    try:
        i = line.strip().split(',')
        x.append(i[0])
        y.append(float(i[1]))
    except ValueError:
        print(f"Skipping line: {line}")
        continue

xTicks = x[::36]

print(f"x: {x}")
print(f"y: {y}")

xAxis, yAxis = plt.subplots()

xAxis.subplots_adjust(bottom = 0.2)

plt.plot(x, y)
plt.xticks(xTicks, rotation = 90)
plt.xlabel('Month')
plt.ylabel('Gas Price')
plt.title('Gas Prices for the Past 30 Years')
plt.savefig('gasPlot.png')
