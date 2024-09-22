import numpy as np


class PBit:
    def __init__(self):
        self.s= 0
        self.update()

    def update(self, i=0):
        self.s = np.sign(np.tanh(i) + self.rand())
        print(self.s)

    @staticmethod
    def rand():
        return np.random.rand()*2 - 1
