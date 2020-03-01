# Ex2
## Cost function and gradient
the regularized cost function in logistic regression is
$$J_(\theta)=\frac{1}{m}\sum_{i=1}^m[-y^{i}\log(h_\theta(x^{(i)})-(1-y^{(i)})\log(1-h_\theta(x^{(i)}))]+\frac{\lambda}{2m}\sum_{j=0}^n
{\theta}_j^2$$
The gradient
of the cost function is a vector where the j
th element is defined as follows:
$$\frac{{\partial J(\theta)}}{\partial \theta_0} = \frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}  \qquad for \quad j=0$$

$$\frac{{\partial J(\theta)}}{\partial \theta_j} = (\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)})+\frac{\lambda}{m}\theta_j  \qquad for \quad j \geq 1$$