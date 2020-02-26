#COMPUTECOST Compute cost for linear regression
#   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
#   parameter for linear regression to fit the data points in X and y

# You need to return the following variables correctly 

# ====================== YOUR CODE HERE ======================
# Instructions: Compute the cost of a particular choice of theta
#               You should set J to the cost.
# # compute and display initial cost

import numpy as np
def computeCost(X,y,theta):
        m = len(y) # Initialize some useful values
        h_x = X.dot(theta).reshape(-1)
        cost = 1/(2*m)*np.sum(np.square(h_x-y))
        return cost

# =========================================================================
