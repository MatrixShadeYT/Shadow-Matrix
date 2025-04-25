from random import randint
import numpy

# Data = [BIAS,[WEIGHTS]]
class neuron:
    def __init__(self,data):
        if isinstance(data,int):
            self.weights = [randint(0,100)/100 for i in range(data)]
            self.bias = randint(0,100)/100
        else:
            self.weights = data[1]
            self.bias = data[0]
    def output(self,inputs):
        output = self.bias
        for i in range(len(inputs)):
            output += inputs[i]*self.weights[i]
        return output
    def getData(self):
        return [self.bias,self.weights]

# Layer [NEURONS] or [[BIAS,[WEIGHTS]]]
class layer:
    def __init__(self,data):
        if isinstance(data[0],int):
            self.neurons = [neuron(data[i]) for i in range(len(data))]
        else:
            self.neurons = data
    def output(self,inputs):
        if isinstance(self.neurons,list):
            output = [self.neurons[i][0] for i in range(len(self.neurons))]
            for i in range(len(output)):
                output[i] += inputs[i]*self.weights[i]
        else:
            output = [self.neurons[i].getData() for i in range(len(self.neurons))]
        return output
    def getData(self):
        if isinstance(self.neurons,list):
            output = self.neurons
        else:
            [self.neurons[i].getData() for i in range(len(self.neurons))]
        return output