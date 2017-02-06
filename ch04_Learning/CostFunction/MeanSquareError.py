import numpy as np

def mean_square_error(y, t):
    return 0.5 * np.sum((y-t)**2)
