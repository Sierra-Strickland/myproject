# import the library that will give us the tools to plot the data
from pylab import *

data = np.loadtxt('gasData.dat')

# x values
x = [1 ,2, 3]

# y values
y = [1, 2, 3]

plot(x, data)
savefig('data.png')
