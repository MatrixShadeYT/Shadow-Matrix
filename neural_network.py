from random import randint
import numpy as np

class model:
    def __init__(self,layers):
        self.layers = layers
    def output(self,inputs):
        inputs = inputs
        for i in range(len(self.layers)):
            inputs = self.layers[i].forward(inputs)
        return inputs

# Layer Class
class Layer_Dense:
    def __init__(self,activation=0,data=5,inputs=1):
        self.activation = activation
        if isinstance(data,int):
            self.weights = 0.1*np.random.randn(data,inputs)
            self.biases = np.zeros((1,data))
        else:
            self.biases, self.weights = data
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