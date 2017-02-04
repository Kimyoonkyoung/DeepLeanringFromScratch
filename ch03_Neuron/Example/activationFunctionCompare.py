import numpy as np
import matplotlib.pylab as plt

# regression
def identity_function(x):
    return x

# classification
def softmax(a):
    max = np.max(a) # prevent overflow
    exp_a = np.exp(a - max)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

# binary classificatyion
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# perceptron
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)

plt.plot(x, y1)
plt.plot(x, y2, 'k--')
plt.ylim(-0.1, 1.1)
plt.show()
