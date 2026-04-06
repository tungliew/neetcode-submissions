import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def train(self, X: NDArray[np.float64], y: NDArray[np.float64], epochs: int, lr: float) -> Tuple[NDArray[np.float64], float]:
        # X: (n_samples, n_features)
        # y: (n_samples,) targets
        # epochs: number of training iterations
        # lr: learning rate
        #
        # Model: y_hat = X @ w + b
        # Loss: MSE = (1/n) * sum((y_hat - y)^2)
        # Initialize w = zeros, b = 0
        # return (np.round(w, 5), round(b, 5))
        # pass

        n_samples, n_features = X.shape

        W = np.zeros(n_features)

        b = 0

        for _ in range(epochs):
            y_hat =  X @ W + b
            # loss = (1/n_samples) * np. sum((y_hat - y)**2)
            dL_dW = (2/n_samples) * X.T @ (y_hat - y)
            dL_db = (2/n_samples) * np.sum(y_hat - y)

            W = W - lr * dL_dW
            b = b - lr * dL_db
        
        
        return (np.round(W, 5), round(b, 5))

            
            
