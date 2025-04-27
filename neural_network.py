from random import randint
import numpy as np

# Model Class - [Layer]
class model:
    def __init__(self,layers):
        self.layers = layers
    def output(self,inputs):
        inputs = inputs
        for i in range(len(self.layers)):
            inputs = self.layers[i].forward(inputs)
        return inputs
    def setData(self,data):
        self.data = data
        for i in range(len(self.layers)):
            self.layers[i].setData(data[i])
    def getData(self):
        self.data = [self.layers[i].getData() for i in range(len(self.layers))]

# Layer Class - [biases,[weights]]
class Layer_Dense:
    def __init__(self,activation=0,data=0,inputs=1):
        self.activation = activation
        if isinstance(data,int):
            self.biases, self.weights = self.generate(data,inputs)
        else:
            self.biases, self.weights = data
    def setData(self,biases,weights):
        self.biases, self.weights = biases, weights
    def getData(self):
        return [self.biases,self.weights]
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)+self.biases
        self.ReLu = np.maximum(0,self.output)
        self.SM = np.exp(self.output-np.max(self.output,axis=1,keepdims=True)) / np.sum(np.exp(self.output-np.max(self.output,axis=1,keepdims=True)),axis=1,keepdims=True)
        if self.activation == 'ReLu':
            return self.ReLu
        elif self.activation == 'SM':
            return self.SM
        else:
            return self.output
    def generate(self,data,inputs):
        self.biases = np.zeros(1,data)
        self.weights = np.random.randn(data,inputs)