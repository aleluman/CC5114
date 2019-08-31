import numpy as np


def sigmoid(x):
    """returns the value of x evaluated on the sigmoid function"""
    return 1 / (1 + np.exp(-x))


def sigmoid_d(x):
    """returns the value of x evaluated on the derivative 
    of the sigmoid function"""
    return sigmoid(x) * (1 - sigmoid(x))


def tanh(x):
    """returns the value of x evaluated on the hyperbolic tangent function"""
    return np.tanh(x)


def tanh_d(x):
    """returns the value of x evaluated on the derivative 
    of the hyperbolic tangent function"""
    return 1 - (tanh(x) ** 2)


def rrelu(x):
    """returns the value of x evaluated on the rectified linear unit function"""
    x = np.maximum(x, 0.01 * x)
    return x


def rrelu_d(x):
    """returns the value of x evaluated on the derivative 
    of the rectified linear unit function"""
    x[x <= 0] = 0.01
    x[x > 0] = 1
    return x
