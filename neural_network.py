from random import randint
import numpy

#Euler's Number
e = 2.718281182846

# Layer Class
class Layer_Dense:
    def __init__(self,inputs=1,data=5,activation=0):
        self.activation = activation
        if isinstance(data,int):
            self.weights = 0.1*numpy.random.randn(inputs,data)
            self.biases = numpy.zeros((1,data))
        else:
            self.biases, self.weights = data
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)+self.biases
        self.ReLu = np.maximum(0,self.output)