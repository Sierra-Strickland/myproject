# importing libraries
import matplotlib.pyplot as plt

try:
    with open('./gasData.dat', 'r', newline = '\r\n') as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found")
    exit()

xData = []
yData = []

for line in data:
    try:
        x, y = line.strip().split(',')
        xData.append(x)
        yData.append(float(y))
    except ValueError:
        print(f"Skipping line: {line}")
        continue

print(f"xData: {xData}")
print(f"yData: {yData}")

plt.plot(xData, yData)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.show()
