from utilities import *
from network import *
from activation_functions import *
import numpy as np
import matplotlib.pyplot as plt


data_x = np.loadtxt("iris.data", delimiter=",", usecols=range(0, 3))
data_x = normalize(data_x)
data_y = np.loadtxt("iris.data", dtype="str", delimiter=",", usecols=[4])
encoding = one_hot_encoding(data_y)
data_y = encode(data_y, encoding)
print(np.shape(data_y))
x_len = np.shape(data_x)[1]
y_len = np.shape(data_y)[1]
data = [[np.reshape(x, (x_len, 1)), np.reshape(y, (y_len, 1))] for x, y in zip(data_x, data_y)]
print(len(data_x))
net = Network([x_len, 15, y_len], tanh, tanh_d, 0.1)
net.train(data, 2000)
plt.plot(net.plotx, net.error)
plt.show()


