from random import randint
import numpy

X = [
    [1.0,2.0,3.0,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]
]

class layer:
    def __init__(self,inputs=1,data=5,activation=0):
        self.activation = activation
        if isinstance(data,int):
            self.weights = 0.1*numpy.random.randn(inputs,data)
            self.biases = numpy.zeros((1,data))
        else:
            self.biases, self.weights = data
    def forward(self,inputs):
        if self.activation == 'ReLu':
            self.output = max(0,np.dot(inputs,self.weights)+self.biases)
        else:
            self.output = np.dot(inputs,self.weights)+self.biases