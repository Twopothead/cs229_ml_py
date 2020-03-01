#PLOTDATA Plots the data points X and y into a new figure 
#   PLOTDATA(x,y) plots the data points with + for the positive examples
#   and o for the negative examples. X is assumed to be a Mx2 matrix.
import matplotlib.pyplot as plt
# Create New Figure

# %%
def plotData(X,y):
    admitted = y.iloc[:,0]>0 # convert dataframe y to series
    not_admitted = y.iloc[:,0]<=0 # convert dataframe y to series
    plt.plot(X[admitted][0],X[admitted][1],format('k+'),linewidth=2,markersize=7)
    plt.plot(X[not_admitted][0],X[not_admitted][1],format('ko'),markerfacecolor='y',markersize=7)
    plt.plot()
    return
# %%
