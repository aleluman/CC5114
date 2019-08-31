from utilities import *
from network import *
from activation_functions import *
import numpy as np

random.seed(3)
data_x = np.loadtxt("seeds_dataset.txt", usecols=range(0, 6))
data_x = normalize(data_x)
data_y = np.loadtxt("seeds_dataset.txt", usecols=[7])
encoding = one_hot_encoding(data_y)
data_y = encode(data_y, encoding)
x_len = np.shape(data_x)[1]
y_len = np.shape(data_y)[1]
data = [[np.reshape(x, (x_len, 1)), np.reshape(y, (y_len, 1))] for x, y in zip(data_x, data_y)]
net = Network([x_len, 10,  y_len], tanh, tanh_d, 0.1)
net.train(data, 5000)
net.plot_results()
