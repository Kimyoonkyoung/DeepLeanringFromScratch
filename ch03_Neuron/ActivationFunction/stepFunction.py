# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def stepFunction(x):
    return np.array(x>0, dtype=np.int)

# example
X = np.arange(-5.0, 5.0, 0.1)
Y = stepFunction(X)

# show graph
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()