# METL
## TP 1
Tientso Ning

### Softmax

1. Define softmax.

Softmax: $\left\{\begin{array}{l}\mathbb{R}^{n} \rightarrow[0,1]^{n} \\ x \mapsto \frac{e^{x}}{\sum_{j=1}^{n} e^{x_{j}}}\end{array}\right.$

With $x=\left(x_{1}, \ldots, x_{n}\right), n \in \mathbb{N}$
$\sum_{k=1}^{n} \operatorname{softmax}(x)=1$

$\operatorname{softmax}(x)_{i}=\frac{e^{x_{i}}}{\sum_{i=1}^{n} x^{j}}$



2. Show softmax is invariant to constants.

Let $x \in \mathbb{R}^{n}, c \in \mathbb{R}^{n}, n \in \mathbb{N}$

n = dim(x), where c is a constant vector.

$\operatorname{softmax}(x+c) i=\frac{e^{\left(x_{i}+c_{i}\right)}}{\sum_{i=1}^{n} e^{\left(x_{i}+c_{j}\right)}}$

$=\frac{e^{x_{i}} e^{c_{i}}}{\sum_{i=1}^{n} e^{x_{j}+c_{j}}}$

$=\frac{e^{c_{i}} e^{x_{i}}}{e^{c_{j}} \sum_{j=1}^{n} e^{x_{j}}}$

Since c is a constant.

$=\frac{e^{x_{i}}}{\sum_{j=1}^{n} e^{x_{i}}}$

$=\operatorname{softmax}(x)_{i}, \forall i \in[1, n]$

$\forall x \in \mathbb{R}^{n}, \forall c \in \mathbb{R}^{n}, \operatorname{softmax}(x+c)=\operatorname{softmax}(x)$



### Sigmoid

1. Define sigmoid and gradient.

sigmoid: $\left\{\begin{array}{l}\mathbb{R}^{n} \rightarrow[-1,1]^{n} \\ x \mapsto \frac{1}{1+e^{-x}}\end{array}\right.$
with $x=\left(x_{1}, \cdots, x_{n}\right), n \in \mathbb{N}$
$\delta(x)=\frac{1}{1+e^{-x_{i}}}$

$\begin{aligned} \frac{d}{d x} \delta(x) &=\frac{d}{d x}\left(\frac{1}{1+e^{-x}}\right) \\ &=\frac{d}{d x}\left(1+e^{-x}\right)^{-1} \\ &=\frac{d}{d x}\left(1+e^{-x}\right)^{-1} \\ &=-\left(1+e^{-x}\right)^{-2}\left(-e^{-x}\right) \\ &=\frac{e^{-x}}{\left(1+e^{-x}\right)^{2}} \\ &=\frac{1}{1+e^{-x}} \cdot \frac{e^{-x}}{1+e^{-x}} \end{aligned}$

$=\frac{1}{1+e^{-x}} \cdot \frac{\left(1+e^{-x}\right)-1}{1+e^{-x}}$
$=\frac{1}{1+e^{-x}} \cdot\left(1-\frac{1}{1+e^{-x}}\right)$
$=\delta(x) \cdot(1-\delta(x))$

2. Derive gradient with respect to CE loss.

$\frac{\partial C E}{\partial \theta}=\hat{y}-y$
$CE=-\sum_{i=1}^{n} y_{i} \log \left(\hat{y}_{i}\right)$

We have a one-hot representation, where we have a 1 at the k-th position, turning the sum into just one line (at the k-th line).

$=-y_{i} \log \left(\hat{y}_{i}\right)$
$=-\log (\operatorname{softmax}(\theta))$

$\frac{\partial C E}{\partial \theta}=\partial\left(-\log \left(\frac{e^{\theta}}{\sum_{i=1}^{n} e^{\theta_{i}}}\right)\right)$

$=\partial\left(-\left(\log e^{\theta}-\log \sum e^{\theta_{i}}\right)\right)$
$=\partial\left(-\theta+\log \sum e^{\theta_{i}}\right)$
$=\partial\left(\log \sum e^{\theta}-\theta_{i}\right)$

$=\frac{1}{\sum e^{\theta}} \cdot \partial\left(\sum e^{\theta_{i}}\right)-y$

$=\frac{e^{\theta_{i}}}{\sum e^{\theta}}-y$
$=\hat{y}-y$

3. Derive the gradients.

$z_{1}=x w_{1}+b_{1}$
$z_{2}=h w_{2}+b_{2}$

$\frac{\partial C E}{\partial z_{2}}=\hat{y}-y$ , from the previous derivations.

$\frac{\partial C E}{\partial h}=(\hat{y}-y) \frac{\partial z_{2}}{\partial h}=(\hat{y}-y) w_{2}^{\top}$

where $\frac{\partial z_{i}}{\partial x_{i}}=W_{i}^{\top}$ since the relationship is that for each layer, we have the weights multiplied by the inputs with a bias. But the bias doesn't affect the derivative calculation, so we just evaluate the relationship with the weight.

$\frac{\partial C E}{\partial z_{1}}=(\hat{y}-y) w_{2}^{T} \frac{\partial h}{\partial z_{1}}=(\hat{y}-y) w_{2}^{T} \odot \theta^{\prime}\left(z_{1}\right)$ since the layer is the application of the sigmoid, in element-wise fashion.

$\frac{\partial C E}{\partial x}=(\hat{y}-y) \omega_{2}^{\top} \odot \theta^{\prime}\left(z_{1}\right) \frac{\partial z_{1}}{\partial x}$

$=(\hat{y}-y) \omega_{2}^{\top} \odot \theta^{2}\left(z_{1}\right) W_{1}^{\top}$

4. The number of parameters is `(Dx + 1)H + (H+1)Dy`
Since Dx is the dimension of x, and the layer `xW1 + b` requires the bias to be of the same shape H, and HDx is the dimension of xW1.
The second part is from the requirement that it matches the output dimensions, since its a one layer NN. Dy corresponds to the output dimension. The bias has to be the same shape Dy, and the layer produces output dimension HDy.
