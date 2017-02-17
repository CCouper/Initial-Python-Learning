import numpy as np #some matplotlib functions require numpy to run
from matplotlib import pyplot as plt

x=[5,6,7,8]
y=[7,3,8,3]

plt.plot(x,y, linewidth=2.0)
plt.title=('Epic Chart')
plt.ylabel('x axis')
plt.xlabel('y axis')

plt.show()
