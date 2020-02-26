#GRADIENTDESCENT Performs gradient descent to learn theta
#   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
#   taking num_iters gradient steps with learning rate alpha

import numpy as np
from computeCost import computeCost # cs229-ex1
def gradientDescent(X, y, theta, alpha, iterations):
    J_history = np.zeros(iterations) # Initialize some useful values
    for j in range(iterations):
        # ====================== YOUR CODE HERE ======================
        # Instructions: Perform a single gradient step on the parameter vector
        #               theta. 
        #
        # Hint: While debugging, it can be useful to print out the values
        #       of the cost function (computeCost) and gradient here.
        #
        # X.shape => (97,2), theta.shape => (2,1) 
        h_x = X.dot(theta)
        h_x = np.array(h_x).reshape(-1)
        m = len(X)
        # XXX theta[0] -= alpha * (1/m) * np.sum((h_x-y)*X[:,0])
        # XXX theta[1] -= alpha * (1/m) * np.sum((h_x-y)*X[:,1])
        # 应当使用np.average()不然会造成精度不对
        theta[0] -= alpha * np.average((h_x-y)*X[:,0])
        theta[1] -= alpha * np.average((h_x-y)*X[:,1])
        J_history[j] = computeCost(X,y,theta)
    return theta,J_history # Save the cost J in every iteration
    # ============================================================        
