# import math
import numpy as np
# z = initial_theta.T * X
def sigmoid(z):
    # g = np.zeros(z.shape) # g = 1/(1+math.e**(-z))
    return np.true_divide(1, 1 + np.exp(-z))
