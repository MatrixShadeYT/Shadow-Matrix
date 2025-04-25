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
    def output(self,input):
        output = self.bias
        for i in range(len(inputs)):
            output += inputs[i]*self.weights[i]
        return output
    def getData(self):
        return [self.bias,self.weights]

# Layer [neurons]

# Model [layers] or [[neurons]]