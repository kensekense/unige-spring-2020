# METL
## TP3
Tientso Ning

### IBM Model 1

1. Calculate the probabilities.

P(das haus ist klein)

P(the house is small)

l = 4

Assuming the most likely alignment under IBM1

= $p(m|l)\cdot\pi(l+1)^{-1}\cdot p(f|e)$

= `(0.7)(0.8)(0.8)(0.4)/5*5*5*5`

= `0.00028672`

P(the house is little)

= $p(m|l)\cdot\pi(l+1)^{-1}\cdot p(f|e)$

= `(0.7)(0.8)(0.8)(0.4)/5^4`

= `0.00028672`

P(small house the is)

= $p(m|l)\cdot\pi(l+1)^{-1}\cdot p(f|e)$

= `(0.4)(0.8)(0.7)(0.8)/5^4`

= `0.00028672`

P(the)

= $p(m|l)\cdot\pi(l+1)^{-1}\cdot p(f|e)$

= `0.7/2`

= `0.35`


The IBM 1 model does not account for order of words (as we can see above, having the same probability for words out of order). Additionally, it does not penalize short translations accordingly, which we see above as well, where the short "the" receives a good score (the highest) compared to the translations before it.

The noisy channel model has a language model component, meaning it can penalize the grammatical aspects of the translation model using this language model concept. As seen before, it would penalize sentence 3, since the language model component will have sentence 3 rank lower due to grammatical incorrectness (compared to 1 or 2).

### IBM Model 2

1. Calculate probabilities.

According to IBM Model 1, p(e1, a1|g) = p(e2, a2|g) since IBM Model 1 doesn't take into account alignment, as we see before in the previous example. Under IBM Model 2, p(e1, a1|g) should be more likely than p(e2, a2|g) since we know that the first translation makes more sense to us, and this is due to the fact that IBM Model 2 takes into account alignment probabilities, and the alignment of the words are a bit more likely under alignment 1.

Provided calculations:

`p(e1, a1|g) = p(m|l)*p(a1|j,l,m)*p(f|e)`

p(a1|j,l,m) =
D(i=1, j=1, l=6, m=5)
D(i=1, j=2, l=6, m=5)
D(i=3, j=3, l=6, m=5)
D(i=4, j=4, l=6, m=5)
D(i=2, j=5, l=6, m=5)
D(i=5, j=6, l=6, m=5)

p(f|e) =
T(naturlich|of)
T(naturlich|course)
T(das|the)
T(Haus|house)
T(ist|is)
T(klein|small)

`p(e2, a2|g) = p(m|l)*p(a2|j,l,m)*p(f|e)`

p(a1|j,l,m) =
D(i=3, j=1, l=6, m=5)
D(i=1, j=2, l=6, m=5)
D(i=1, j=3, l=6, m=5)
D(i=5, j=4, l=6, m=5)
D(i=2, j=5, l=6, m=5)
D(i=4, j=6, l=6, m=5)

p(f|e) =
T(naturlich|of)
T(naturlich|course)
T(das|the)
T(Haus|house)
T(ist|is)
T(klein|small)

2. Most probable alignment under Model 2 can be computed efficiently if we follow fast_align:
  - For each i = 1, 2, ..., $l_{e}$ that is an empty word (dropped in translation), we consider it null with probability $p_{0}$
  - If not, we use the log-linear distribution $\frac{e^{\lambda h(i, j)}}{Z_{\lambda}(i)}$ to choose a value for $a_{i}$
  - For each j = 1, 2, ..., $l_{e}$ choose a output word $e_{j}$ according to t($e_{j}$|$f_{a(j)}$)

  $a(j | i)=\left\{\begin{array}{ll}p_{0}, & j=0 \\ \left(1-p_{0}\right) \times \frac{e^{\lambda h(i, j)}}{Z_{\lambda}(i)}, & 0<j \leq n \\ 0, & \text { otherwise }\end{array}\right.$

  $h(i, j, m, n)=-\left|\frac{i}{m}-\frac{j}{n}\right|$

  $Z_{\lambda}=\sum_{j=1}^{n} \exp (\lambda h(i, j))$

  We then are able to use these values in the E-step of the EM Algorithm

  $p(\mathbf{e} | \mathbf{f})=\prod_{i=1}^{m} p\left(e_{i} | \mathbf{f}\right)=\prod_{i=1}^{m} \sum_{j=0}^{n} a(j | i) t\left(e_{i} | f_{j}\right), p(a | \mathbf{e}, \mathbf{f})=\frac{p(a, \mathbf{e}, \mathbf{f})}{p(\mathbf{e}, \mathbf{f})}$

  The big-picture here is that originally, the Model 2 alignment probabilities are calculated based on parameters that are independent on each of the positions of the word in alignment, all conditioned on the lengths and positions, making it inefficient. The fast_align method instead calculates the parameters using a log-linear method.
