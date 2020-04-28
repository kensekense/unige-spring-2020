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

sigmoid: $\left\{\begin{array}{l}\mathbb{R}^{n} \rightarrow[0,1]^{n} \\ x \mapsto \frac{1}{1+e^{-x}}\end{array}\right.$
with $x \in \mathbb{R}, n \in \mathbb{N}$
$\sigma(x)=\frac{1}{1+e^{-x_{i}}}$

$\begin{aligned} \frac{d}{d x} \sigma(x) &=\frac{d}{d x}\left(\frac{1}{1+e^{-x}}\right) \\ &=\frac{d}{d x}\left(1+e^{-x}\right)^{-1} \\ &=\frac{d}{d x}\left(1+e^{-x}\right)^{-1} \\ &=-\left(1+e^{-x}\right)^{-2}\left(-e^{-x}\right) \\ &=\frac{e^{-x}}{\left(1+e^{-x}\right)^{2}} \\ &=\frac{1}{1+e^{-x}} \cdot \frac{e^{-x}}{1+e^{-x}} \end{aligned}$

$=\frac{1}{1+e^{-x}} \cdot \frac{\left(1+e^{-x}\right)-1}{1+e^{-x}}$
$=\frac{1}{1+e^{-x}} \cdot\left(1-\frac{1}{1+e^{-x}}\right)$
$=\sigma(x) \cdot(1-\sigma(x))$

2. Derive gradient with respect to CE loss.

$CE=-\sum_{i}^{n} y_{i} \log \left(\hat{y}_{i}\right)$

$\frac{\partial CE}{\partial z}=-\sum_{k} y_{k} \log (\hat{y}_{k})$

$=-\sum_{k} y_{k} \cdot \frac{\partial \log \left(\hat{y}_{k}\right)}{\partial \hat{y}_{k}} \times \frac{\partial \hat{y}_{k}}{\partial z}$

$=-\sum_{k} y_{k} \frac{1}{\hat{y}_{k}} \times \frac{\partial \hat{y}_{k}}{\partial z}$

Since we can have i = k and i != k,

$=-y_{i}\left(1-\hat{y}_{i}\right)-\sum_{k \neq i} y_{k} \frac{1}{\hat{y}_{k}}\left(-\hat{y}_{k} \cdot \hat{y}_{i}\right)$

$=-y_{i}\left(1-\hat{y}_{i}\right)+\sum_{k \neq 1} y_{k} \cdot \hat{y}_{k}$

$=-y_{i}+y_{i} \hat{y}_{i}+\sum_{k \neq 1} y_{k} \cdot \hat{y}_{k}$

$=\hat{y}_{i}\left(y_{i}+\sum_{k \neq 1} y_{k}\right)-y_{i}$

Due to the one-hot encoding, we will have the values inside the parenthesis equal to 1, making the final form:

$=\hat{y}_{i}-y_{i}$

3. Derive the gradients.

$z_{1}=x w_{1}+b_{1}$
$z_{2}=h w_{2}+b_{2}$

$\frac{\partial C E}{\partial z_{2}}=\hat{y}-y$ , from the previous derivations.

$\frac{\partial C E}{\partial h}=(\hat{y}-y) \frac{\partial z_{2}}{\partial h}=(\hat{y}-y) w_{2}^{\top}$

where $\frac{\partial z_{i}}{\partial x_{i}}=w_{i}^{\top}$ .

Note that the jacobian $\frac{\partial z_{2}}{\partial h} = \frac{\partial}{\partial h} \sum W_{2}h = \sum W_{2} \frac{\partial h}{\partial h} = W_{2}$ and that since we are taking the row order, we use $W_{2}^T$

$\frac{\partial C E}{\partial z_{1}}=(\hat{y}-y) w_{2}^{T} \frac{\partial h}{\partial z_{1}}=(\hat{y}-y) w_{2}^{T} \odot \sigma^{\prime}\left(z_{1}\right)$ since the layer is the application of the sigmoid, in element-wise fashion.

$\frac{\partial C E}{\partial x}=(\hat{y}-y) w_{2}^{\top} \odot \sigma^{\prime}\left(z_{1}\right) \frac{\partial z_{1}}{\partial x}$

$=(\hat{y}-y) w_{2}^{\top} \odot \sigma^{2}\left(z_{1}\right) w_{1}^{\top}$

4. The number of parameters is `(Dx + 1)H + (H+1)Dy`
Since Dx is the dimension of x, and the layer `xW1 + b` requires the bias to be of the same shape H, and HDx is the dimension of xW1.
The second part is from the requirement that it matches the output dimensions, since its a one layer NN. Dy corresponds to the output dimension. The bias has to be the same shape Dy, and the layer produces output dimension HDy.
