library(plgp)
n <- 8 #see what happens when you change n, y, or m
#when n changes, the amplitude of the gray lines also changes. Dropping the number makes the amplitude larger.
x <- matrix(seq(0,2*pi, length=n), ncol=1)
y <- sin(x)
#y <- c(1,3,2,5,5,7,3,4)
D <- distance(x)
ep_yy <- exp(-D) + diag(1e-8,ncol(D)) #modified, and when you have the value at 0.001 it scrambles the smoothness of the gray lines
m <- 100 #when m changes to be smaller, the gray lines become more jagged, and the higher, the smoother the curve.
x_star <- matrix(seq(-0.5, 2*pi + 0.5, length=m), ncol=1)
D_starstar <- distance(x_star)
ep_ystarystar <- exp(-D_starstar) + diag(1e-8, ncol(D_starstar))#modified, and when you have the value at 0.001 it scrambles the smoothness of the gray lines
D_star <- distance(x_star, x)
ep_ystary <- exp(-D_star)
ep_yy_inv <- solve(ep_yy)
A <- ep_ystarystar - ep_ystary%*%ep_yy_inv%*%t(ep_ystary)
b <- ep_ystary%*%ep_yy_inv%*%y
sample <- 100
y_star <- rmvnorm(sample, b, A)

#plotting
matplot(x_star, t(y_star), type="l", col="gray", lty=1, xlab="x", ylab="y")
points(x,y, pch=20, cex=2)
lines(x_star, b, lwd=2)
lines(x_star, sin(x_star), col="blue")

q1 <- b + qnorm(0.05, 0, sqrt(diag(A)))
q2 <- b + qnorm(0.95, 0, sqrt(diag(A)))

lines(x_star, q1, lwd=2, lty=2, col="red")
lines(x_star, q2, lwd=2, lty=2, col="red")


#after changing x to be the same period as x_star,
x_star[3] == x[2]
b[3]
y[2]
var(y_star[,3],y_star[,2])

#is the interpolation linear or non-linear?

#if you take all the x_star = x, then you get no values out and only get the values at x. And A becomes close to 0.
