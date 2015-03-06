import matplotlib.pyplot as plt
import numpy as np
import extrema

#Create some random x and y values
x = 2 * np.pi * np.linspace(-1,1,100)
y = np.cos(x) - 0.5 + 0.5 * np.random.random(size=x.shape)
#Add a flat line to the signal
y [39:45] = 1.85
#Add some 'nan'
y[49:53] = float('nan')

#call the extrema function with the signal as parameter
[ymax, ymin, imax, imin] = extrema.extrema(y)

#plot the results
plt.plot(x,y,'k',x[imax], ymax, 'go', x[imin], ymin, 'ro')
plt.show()
