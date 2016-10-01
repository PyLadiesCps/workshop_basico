import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*pi, 2*pi, 0.5) # igual ao range p/ floats
y = np.cos(x)

plt.plot(x,y)
plt.show()
