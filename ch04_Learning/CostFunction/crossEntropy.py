import numpy as np


# one-hot encoding
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]

    delta = 1e-7 # prevent NAN
    return -np.sum(t * np.log(y + delta)) / batch_size

# label
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]

    delta = 1e-7 # prevent NAN
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size

"""
np.arage(3) 은
3크기의 배열을 생성함

t = [2,5,7] 일때
y[np.arange(3), t] 는

y[0,2] y[1,5] y[2,7] 이런식으로 2차원인 y배열의 원소에 접근함
"""