from random import randint
import numpy

class layer:
    def __init__(self,data):
        self.biases, self.weights = data
    def output(self,inputs):
        return numpy.dot(self.weights*inputs) + self.biases
    def getData(self):
        return self.neurons