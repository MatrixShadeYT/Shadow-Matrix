from random import randint
import numpy as np

# Layer Class
class Layer_Dense:
    def __init__(self,inputs=1,data=5):
        self.activation = activation
        if isinstance(data,int):
            self.weights = 0.1*np.random.randn(inputs,data)
            self.biases = np.zeros((1,data))
        else:
            self.biases, self.weights = data
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights)+self.biases
        self.ReLu = np.maximum(0,self.output)
        self.SM = np.exp(self.output-np.max(self.output,axis=1,keepdims=True)) / np.sum(np.exp(self.output-np.max(self.output,axis=1,keepdims=True)),axis=1,keepdims=True)
