# coding: utf-8
import numpy as np

def softmax(a):
    max = np.max(a)

    exp_a = np.exp(a - max) #오버플로우 피하기 위해서, 입력값의 max 값으로 모든 원소들을 빼줌
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

