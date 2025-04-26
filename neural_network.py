from random import randint
import numpy

class layer:
    def __init__(self,data):
        if isinstance(data,list):
            self.biases, self.weights = data
        else:
            self.weights = []
            for i in range(data):
                self.weights.append([randint(0,100)/100 for i in range(data)])
            self.biases = [randint(0,100)/100 for i in range(data)]
    def output(self,inputs):
        return numpy.dot(self.weights*inputs) + self.biases
    def neuron(self,num,bias,weights):
        self.weights[num] = weights
        self.baises[num] = bias
    def getData(self):
        return self.neurons

class model:
    def __init__(self,layers):
        self.layers = layers
    def output(self,inputs):
        inputs = inputs
        for i in range(len(self.layers)):
            inputs = self.layers[i].output(inputs)
        return inputs