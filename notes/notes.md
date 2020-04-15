# cs229_ml_py
[正常查看其教程，需要准备好jupyter notebook所需环境](https://blog.csdn.net/u011602557/article/details/103661581)
```bash
pip install jupyter_latex_envs --upgrade
jupyter nbextension install --py latex_envs --user
jupyter nbextension enable latex_envs --user --py
```
## ex1
%run
用%run函数在notebook中运行一个python脚本试试。
由于ipynb占空间，我还是写py上传
可以写时用ipynb，然后每次上传之前导出。配置多级gitnore，忽略ipynb不提交。
## ex2
我的错误之处在于不应该用test_theta.T * X而应该用X.dot(test_theta)
前者shape是(100, 3)，后者shape (100,1)
- Youtube视频：Statistics 101: Logistic Regression, An Introduction
- [fminunc-找到最小的无约束多变量函数](https://www.jianshu.com/p/f08db2e1a0a9)
```
min f(x)
x
```
where f(x) is a function that returns a scalar（标量）.
x is a vector or a matrix;
### fminunc (Matlab)
x = fminunc（fun，x0）从x0开始，尝试寻找fun中描述的函数的局部最小值x。 点x0可以是标量，矢量或矩阵

x = fminunc（fun，x0，options）使选项中指定的优化选项最小化。 使用optimoptions来设置这些选项。

x = fminunc(problem) finds the minimum for problem, where problem is a structure described in Input Arguments. Create the problem structure by exporting a problem from Optimization app, as described in Exporting Your Work.
### fmin (scipy)
[optimize]https://www.jianshu.com/p/2ec8e6b76e36
fmin优化方法没用到偏导
fmin(func, x0, args=(), xtol=0.0001, ftol=0.0001, maxiter=None, maxfun=None, full_output=0, disp=1, retall=0, callback=None, initial_simplex=None)
### minimize (scipy)
开始试过scipy里的fmin，好像不太好用，换成minimize函数
[使用scipy.optimize.minimize()时遇到的问题](https://blog.csdn.net/TianJingDeng/article/details/103796772)
np.info(minimize)
### [Python fminunc 的替代方法](https://blog.csdn.net/csdn_inside/article/details/81558079)
- 需要注意的是fun关键词参数里面的函数，需要把优化的theta放在第一个位置，X,y，放到后面。并且，theta在传入的时候一定要是一个一维shape（n,）的数组，不然会出错。
(n,1)的列向量 -> (n,)
### legend
[matplotlib6 -- 添加 图例 legend](https://blog.csdn.net/dss_dssssd/article/details/84454112)
[Numpy：取消numpy数组默认以科学计数法显示](https://www.jianshu.com/p/90144d5fc985)

##  Ex3
- [python将每一次变量值赋给矩阵，矩阵分块从大矩阵中遍历固定大小的所有小矩阵](https://blog.csdn.net/qq_22472089/article/details/89375319)
- [Octave Plot无反应 解决方案](https://blog.csdn.net/zjcxhswill/article/details/81507432)
setenv('GNUTERM','qt')

## matlab的reshape的列优先原则
```matlab
reshape(1:15,5,3)
```
12345会是竖着排列
而python默认会恨着排列
```python
np.arange(1,16).reshape((5,3))
```
[python基础之numpy.reshape详解](https://www.jianshu.com/p/fc2fe026f002)
“F”是指用FORTRAN类索引顺序读/写元素
```python
np.arange(1,16).reshape((5,3),order='F')
```
## References
- [给Python加Markdown式排版，在线运行可做Jupyter替身丨谷歌大脑出品](https://zhuanlan.zhihu.com/p/76875787)
- [详解10个可以快速用Python进行数据分析的小技巧](https://zhuanlan.zhihu.com/p/71034581)