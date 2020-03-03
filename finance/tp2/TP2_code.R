#Tientso Ning
#Series 2

set.seed(0);
n=10000;
a1=rnorm(n,mean=0,sd=1);
a2=rnorm(n,mean=0,sd=2);

X = a1 + 2*a2;
Y = 2*a1 + a2;

#compute the correlation between X and Y
print(cor(X,Y));

#display the graph of X and Y
plot(X,Y);

#compute the ACF
T = 10;
x <- rnorm(100) + sin(2*pi*1:100/T);
plot(x, type='l')
T = 50;
x <- rnorm(100) + sin(2*pi*1:100/T);
plot(x, type='l')
T = 100;
x <- rnorm(100) + sin(2*pi*1:100/T);
plot(x, type='l')
