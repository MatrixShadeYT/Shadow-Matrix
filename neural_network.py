from random import randint
import numpy as np

class Loss:
    def calculate(self,output,y):
        return np.mean(self.forward(output,y))

class LCC(Loss):
    def forward(self,y_pred,y_true):
        return -np.log(np.clip(y_pred,1e-7,1-1e-7)[range(len(y_pred)),y_true] if len(y_true.shape) == 1 elif len(y_true.shape) == 2: np.sum(np.clip(y_pred,1e-7,1-1e-7)*y_true,axis=1))

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
