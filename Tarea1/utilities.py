import numpy as np


def normalize(array, nh=1, nl=0):
    return (array - array.min(0)) * ((nh - nl) / array.ptp(0)) + nl


def one_hot_encoding(array):
    labels = np.unique(array)
    number_of_labels = labels.size
    encoded = {}
    for i in range(number_of_labels):
        encoding = np.zeros(number_of_labels)
        encoding[i] = 1
        encoded[labels[i]] = encoding
    return encoded


def encode(array, encoding):
    encoded = []
    for i in array:
        encoded.append(encoding[i])
    return encoded


def load_data_wrapper(name, input_cols, output_col, output_type="float", delimiter=None):
    data_x = np.loadtxt(name, usecols=input_cols, delimiter=delimiter)
    data_x = normalize(data_x)
    data_y = np.loadtxt(name, usecols=output_col, delimiter=delimiter, dtype=output_type)
    encoding = one_hot_encoding(data_y)
    data_y = encode(data_y, encoding)
    x_len = np.shape(data_x)[1]
    y_len = np.shape(data_y)[1]
    data = [[np.reshape(x, (x_len, 1)), np.reshape(y, (y_len, 1))] for x, y in zip(data_x, data_y)]
    return data, x_len, y_len
