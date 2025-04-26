from random import randint
import numpy

class layer:
    def __init__(self,data):
        if data:
            self.biases, self.weights = data
        else:
            self.weights = []
            for i in range(data):
                self.weights.append([randint(0,100)/100 for i in range(data)])
            self.biases = [randint(0,100)/100 for i in range(data)]
    def output(self,inputs):
        return numpy.dot(self.weights*inputs) + self.biases
    def getData(self):
        return self.neurons