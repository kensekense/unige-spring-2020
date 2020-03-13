# METL TP 1
Tientso Ning

## Softmax
##### 1. Clearly redefine the softmax function:
$\operatorname{softmax}(\mathrm{X})=\frac{e^{x_{i}}}{\sum_{j=1}^{n} e^{x_{j}}},$ where $x \in X$


##### 2. Show that the softmax is invariant to constant offsets.
If we examine:

$\begin{aligned} \operatorname{softmax}(x)=& \operatorname{softmax}(x+c) \\ e^{x_{i}+c} &=e^{x_{i}} e^{c} \\ \sum_{j=1}^{n} e^{x_{j}+c} &=e^{c} \sum_{j=1}^{n} e^{x_{j}} \end{aligned}$

We notice that the value e<sup>c</sup> our additionally added constant value, will cancel out, showing that our function is invariant to this offset.

##### 3. Please see code.

## Gradient, Sigmoid, Forward, Backward
##### 1. Define the sigmoid function and derive the gradients.
We define the sigmoid function as such:

$\sigma(X)=\frac{1}{1+e^{-x_{i}}},$ where $x \in X, X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$

And derive the gradients:

$\begin{aligned} \frac{d}{d x} \sigma(x) &=\frac{d}{d x}\left[\frac{1}{1+e^{-x}}\right] \\ &=\frac{d}{d x}\left(1+\mathrm{e}^{-x}\right)^{-1} \\ &=-\left(1+e^{-x}\right)^{-2}\left(-e^{-x}\right) \\ &=\frac{e^{-x}}{\left(1+e^{-x}\right)^{2}} \\ &=\frac{1}{1+e^{-x}} \cdot \frac{e^{-x}}{1+e^{-x}} \\ &=\frac{1}{1+e^{-x}} \cdot \frac{\left(1+e^{-x}\right)-1}{1+e^{-x}} \\ &=\frac{1}{1+e^{-x}} \cdot\left(\frac{1+e^{-x}}{1+e^{-x}}-\frac{1}{1+e^{-x}}\right) \\ &=\frac{1}{1+e^{-x}} \cdot\left(1-\frac{1}{1+e^{-x}}\right) \\ &=\sigma(x) \cdot(1-\sigma(x)) \end{aligned}$


##### 2. Derive the gradient to the inputs of the softmax function when cross-entropy loss is used.
We know that since we have a one-hot vector representation of the input vector, we can essentially evaluate loss as:

$-\log \left(q_{y}\right)=-\log \left(\frac{e^{x_{y}}}{\sum_{j} e^{x_{j}}}\right)=-x_{y}+\log \sum_{j} e^{x_{j}}$

Since the values where we have zero will cause the entropy calculation to zero out (due to the product with zero) and we only have to evaluate the second part with the log. We insert the softmax function, and apply the rule of log division, and rearrange and agree signs to get the representation ready for gradient calculation.

Then we can calculate the gradient for each x<sub>i</sub>:

$Loss =\nabla_{x_{i}} \log \sum_{j} e^{x_{j}}-\nabla_{x_{i}} x_{y}$
$=\frac{1}{\sum_{j} e^{x_{j}}} \nabla_{x_{i}} \sum_{j} e^{x_{j}}-\nabla_{x_{i}} x_{y}$
$=\frac{e^{x_{i}}}{\sum_{j} e^{x_{j}}}-\nabla_{x_{i}} x_{y}$
$=q_{i}-\nabla_{x_{i}} x_{y}$
$=q_{i}-1(y=1 if y=i, else y=0)$

##### 3. Derive the gradients when we have a one-hidden-layer neural network (perceptron).
We can calculate the gradient as such:
- ...

##### 4. How many parameters are there in this neural network?
Since there are H hidden units, we can consider the parameters to be the weights of that layer of the neural network, and say that there are H parameters.

##### 5. - 7. Code Section
Please check the code for implementation for this section.
