import numpy as np

class LogisticRegression():
    '''
    Logistic Regression class
    '''
    
    def __init__(self):
        
        self.loss_history = []
        
        self.score_history = []
        
        self.w = []
        
    
    def predict(self, X):
        return X@self.w
    
    
    def sigmoid(self, z):
        '''
        Logistic sigmoid function
        '''
        return 1 / (1 + np.exp(-z))
    
    
    def logistic_loss(self, y_hat, y):
        return -y*np.log(self.sigmoid(y_hat)) - (1-y)*np.log(1-self.sigmoid(y_hat))
    
    
    def empirical_risk(self, X, y):
        '''
        aka 'loss'
        '''
        y_hat = self.predict(X)
        
        return self.logistic_loss(y_hat, y).mean()
    
    
    def gradient(self, X, y):
        '''
        Calculate the gradient
        '''
        grad = 0
        
        for i in range(X.shape[0]):
            X_i = X[i,:]
            y_i = y[i]
            
            grad += (1/X.shape[0]) * ((self.sigmoid(np.dot(self.w, X_i)))-y_i) * X_i
            
        return grad
    
    
    def score_calc(self, X, y):
        
        return (y == (self.predict(X)>0)).mean()
    
    
    def fit(self, X, y, alpha, max_epochs):
        '''
        Args:
            X --> training vectors
            y --> target variables
            alpha --> learning rate
            max_epochs --> max iterations
        '''
        
        # add ones to X
        X_ = np.append(X, np.ones((X.shape[0], 1)), 1)
        
        # weight vector
        self.w = np.random.rand(X.shape[1]+1)
        
        for i in range(max_epochs):
            
            self.score_history.append(self.score_calc(X_, y))
            
            self.loss_history.append(self.empirical_risk(X_, y))
            
            w_f = self.w - (alpha * self.gradient(X_, y))
            
            self.w = w_f
            
    
    def fit_stochastic(self, X, y, alpha, batch_size, max_epochs):
        '''
        Args:
            X --> training vectors
            y --> target variables
            alpha --> learning rate
            batch_size --> number of data split into batches
            max_epochs --> max iterations
        '''
        # add ones to X
        X_ = np.append(X, np.ones((X.shape[0], 1)), 1)
        
        # weight vector
        self.w = np.random.rand(X.shape[1] + 1)
        
        for j in np.arange(max_epochs):
            
            order = np.arange(X.shape[0])
            np.random.shuffle(order)
            
            for batch in np.array_split(order, X.shape[0] // batch_size + 1):
                
                x_batch = X[batch,:]
                y_batch = y[batch]
                
                w_f = self.w - (alpha * self.gradient(X_, y))
                self.w = w_f
                
            self.score_history.append(self.score_calc(X_, y))
            self.loss_history.append(self.empirical_risk(X_, y))
