import numpy as np
import random


class Network:
    def __init__(self, layers, activation_function, derivative, learning_rate):
        self.layers = layers
        self.activation_function = activation_function
        self.derivative = derivative
        self.learning_rate = learning_rate
        self.biases = [np.random.randn(y, 1) for y in layers[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(layers[:-1], layers[1:])]
        self.plotx = []
        self.ploty = []
        self.error = []

    def feed(self, inp):
        for bias, weight in zip(self.biases, self.weights):
            inp = self.activation_function(np.dot(weight, inp) + bias)
        return inp

    def loss(self, data):
        calculated_output = np.array([self.feed(sample[0]) for sample in data])
        real_output = [sample[1] for sample in data]
        loss = ((calculated_output - real_output) ** 2).mean()
        return loss

    def backward_propagation(self, x, y):
        dB = [np.zeros(b.shape) for b in self.biases]
        dW = [np.zeros(w.shape) for w in self.weights]
        z_vectors = []
        activation = x
        output_by_layer = [x]
        for bias, weight in zip(self.biases, self.weights):
            z = np.dot(weight, activation) + bias
            activation = self.activation_function(z)
            z_vectors.append(z)
            output_by_layer.append(activation)
        delta_d = (output_by_layer[-1] - y) * self.derivative(z_vectors[-1])
        dB[-1] = delta_d
        dW[-1] = np.dot(delta_d, output_by_layer[-2].T)
        for layer in range(2, len(self.layers)):
            z = z_vectors[-layer]
            delta_d = np.dot(self.weights[-layer + 1].T, delta_d) * self.derivative(z)
            dB[-layer] = delta_d
            dW[-layer] = np.dot(delta_d, output_by_layer[-layer - 1].T)
        return dB, dW

    def update_parameters(self, data):
        dB = [np.zeros(bias.shape) for bias in self.biases]
        dW = [np.zeros(weight.shape) for weight in self.weights]
        for x, y in data:
            d_dB, d_dW = self.backward_propagation(x, y)
            dB = [db + ddb for db, ddb in zip(dB, d_dB)]
            dW = [dw + ddw for dw, ddw in zip(dW, d_dW)]
        self.weights = [w - (self.learning_rate / len(data)) * dw for w, dw in zip(self.weights, dW)]
        self.biases = [b - (self.learning_rate / len(data)) * db for b, db in zip(self.biases, dB)]

    def train(self, data, iterations):
        random.shuffle(data)
        partition = (len(data) // 10) * 8
        test_data = data[partition:]
        training_data = data[:partition]
        for i in range(iterations):
            random.shuffle(training_data)
            self.update_parameters(training_data)
            correct = self.evaluate(test_data)
            print("Epoch {} : {} / {}".format(i, correct, len(test_data)))
            self.plotx.append(i)
            self.ploty.append(correct)
            self.error.append(self.loss(training_data))

    def evaluate(self, data):
        test_results = [np.argmax(self.feed(sample[0]))for sample in data]
        real_outputs = [np.argmax(sample[1]) for sample in data]
        return sum(int(x == y) for (x, y) in zip(test_results, real_outputs))
