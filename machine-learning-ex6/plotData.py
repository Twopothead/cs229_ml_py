#PLOTDATA Plots the data points X and y into a new figure 
#   PLOTDATA(x,y) plots the data points with + for the positive examples
#   and o for the negative examples. X is assumed to be a Mx2 matrix.
import matplotlib.pyplot as plt
# Create New Figure
import numpy as np
# %%
def plotData(X,y):
    # plt.plot(X[(y>0).reshape(-1)][:,0],X[(y>0).reshape(-1)][:,1],format('k+'),linewidth=2,markersize=7)
    # plt.plot(X[(y==0).reshape(-1)][:,0],X[(y==0).reshape(-1)][:,1],format('ko'),markerfacecolor='y',markersize=7)
    # pos = np.arange(y.shape[0])[y.reshape(-1)==1]
    # neg = np.arange(y.shape[0])[y.reshape(-1)==0]
    pos = (y>0).reshape(-1)
    neg = (y==0).reshape(-1)
    plt.plot(X[pos][:,0],X[pos][:,1],'k+',markersize=7,linewidth=1)
    plt.plot(X[neg][:,0],X[neg][:,1],'ko',markerfacecolor='y',linewidth=1)
    plt.plot()
    return
# %%
