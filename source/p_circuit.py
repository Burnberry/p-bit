import numpy as np


class PCircuit:
    def __init__(self, biases, weights):
        self.biases = np.array(biases)
        self.outputs = np.zeros(len(biases))
        self.weights = np.array(weights)

        # init outputs
        self.update()

    def update(self):
        inputs = np.linalg.matmul(self.weights, self.outputs) + self.biases
        self.outputs = np.sign(np.tanh(inputs) + self.get_random())
        print(self.outputs, sum(self.outputs))

    def get_random(self):
        return np.random.random(len(self.outputs))*2 - 1

