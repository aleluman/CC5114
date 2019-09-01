import numpy as np


def normalize(matrix, nh=1, nl=0):
    """Normalizes each column in a matrix by calculating its maximum
    and minimum values, the parameters nh and nl specify the final range
    of the normalized values"""
    return (matrix - matrix.min(0)) * ((nh - nl) / matrix.ptp(0)) + nl


def one_hot_encoding(array):
    """Encodes each unique label in 'array' in a vector of the same length as
    the number of unique labels. This vector is filled with zeros and a 1
    representing the position assigned to the label"""
    labels = np.unique(array)
    number_of_labels = labels.size
    encoded = {}
    for i in range(number_of_labels):
        encoding = np.zeros(number_of_labels)
        encoding[i] = 1
        encoded[labels[i]] = encoding
    return encoded


def encode(array, encoding):
    """Encodes 'array' with the encoding specified in encoding.
    This value must be a dictionary"""
    encoded = []
    for i in array:
        encoded.append(encoding[i])
    return encoded


def load_data_wrapper(name, input_cols, output_col, output_type="float", delimiter=None):
    """Wrapper to load the desired data in an easier way. It returns the normalized and encoded
    data, alongside with the size of the values in the inputs and outputs to initialize
    the neural network correctly"""
    data_x = np.loadtxt(name, usecols=input_cols, delimiter=delimiter)
    data_x = normalize(data_x)
    data_y = np.loadtxt(name, usecols=output_col, delimiter=delimiter, dtype=output_type)
    encoding = one_hot_encoding(data_y)
    data_y = encode(data_y, encoding)
    # x_len will be the number of input neurons, and y_len the number of output neurons
    x_len = np.shape(data_x)[1]
    y_len = np.shape(data_y)[1]
    data = [[np.reshape(x, (x_len, 1)), np.reshape(y, (y_len, 1))] for x, y in zip(data_x, data_y)]
    return data, x_len, y_len
