# Ex3
## Vectorizing Logistic Regression
in (unregularized) logistic regression, the cost function is
$$J_(\theta)=\frac{1}{m}\sum_{i=1}^m[-y^{i}\log(h_\theta(x^{(i)})-(1-y^{(i)})\log(1-h_\theta(x^{(i)}))]$$
To compute each element in the summation, we have to compute $h_\theta(x^{(i)})$ for every example i, where $h_\theta(x^{(i)})=g(\theta^Tx^{(i)})$ and $g(z)=\frac{1}{1+e^{-z}}$