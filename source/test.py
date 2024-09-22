import numpy as np
import math

from source.p_bit import PBit
from source.p_circuit import PCircuit


def test():
    parent_test()


def parent_test():
    biases = [0, 0]
    weights = [[10, 0],
               [1, 0]]
    circuit = PCircuit(biases, weights)
    for i in range(100):
        circuit.update()
