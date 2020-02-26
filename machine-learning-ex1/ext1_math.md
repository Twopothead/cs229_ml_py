# Ex1
## Gradient Descent
The objective of linear regression is to minimize the cost function
$$J(\theta)=\frac{1}{2m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})^2$$
where the hypothesis $h_\theta(x)$ is given by the linear model
$$h_\theta(x)=\theta^{T}x=\theta_0+\theta_1x_1$$
### Batch gradient descent
- param : $\theta_i$

$$\theta_j := \theta_j - \alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}$$
