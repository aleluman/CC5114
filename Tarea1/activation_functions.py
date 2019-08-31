import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_d(x):
    return sigmoid(x) * (1 - sigmoid(x))


def tanh(x):
    return np.tanh(x)


def tanh_d(x):
    return 1 - (tanh(x) ** 2)


def rrelu(x):
    x = np.maximum(x, 0.01 * x)
    return x


def rrelu_d(x):
    x[x < 0] = 0.01
    x[x >= 0] = 1
    return x
