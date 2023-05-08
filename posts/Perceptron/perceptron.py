import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs

class Perceptron(object):
    '''
    perceptron class
    '''
    def __init__(self):
        self.history = []
        self.w = []
        
        
    def predict(self, X):
        
        X_ = np.append(X, np.ones((X.shape[0], 1)), 1)
        
        return X_@self.w >= 0

    
    def score(self, X, y):
        '''
        This is the function that shows the accuracy of the perceptron algorithm
        
        Args:
            X --> training vectors
            y --> target variables
        '''
        s = np.sum(y == self.predict(X)) / y.shape[0]
        
        return s
  
    
    def fit(self, X, y, max_steps=1000):
        '''
        Args:
            X --> training vectors
            y --> target variables
            max_steps --> maximum steps
        '''
        
        # add ones to X
        X_ = np.append(X, np.ones((X.shape[0], 1)), 1)
        
        # weight vector
        self.w = np.random.rand(X.shape[1]+1)
   
        #self.history = []
    
        for i in range(max_steps):
            # perform the perceptron update and log the score in self.history
            
            # Calculate score and append to history
            self.history.append(self.score(X, y))
            
            # Pick a random index
            j = np.random.randint(X.shape[0]-1) 
            
            X_j = X_[j]
            y_j = 2*y[j]-1      # Given in the blog post guide
            
            # Calculate the new weight as given in the guide
            w_f = self.w + (y_j*np.dot(self.w, X_j) < 0) * (y_j * X_j)
            
            # Update the weights with the final
            self.w = w_f