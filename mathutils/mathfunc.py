# coding:utf-8
import numpy as np

# https://en.wikipedia.org/wiki/Sigmoid_function
def sigmoid(x):
    return 1/(1+np.exp(x*(-1)))
