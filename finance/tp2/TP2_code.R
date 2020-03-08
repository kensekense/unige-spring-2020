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

#read the priceM.dat file as a table, location will vary

ret <- function(x){
  i = 1
  rets <- c()

  for(val in x){
    if (i == 1){
      calc <- 0
    }
    else{
      calc <- (x[i]-x[i-1])/x[i-1] #returns
    }
    rets <- c(rets, calc)
    i = i+1
  }
  return(rets)
}

tab <- read.table("C:/Users/liveo/Desktop/playground/unige-spring-2020/finance/tp2/priceM.dat")
tab[[1]] = tab[[1]]/1000

ar(tab[[2]])
