#define a function to calculate returns on a vector
mret <- function(x) {
  sol <- c() #create a list to hold monthly returns

  i <- 1
  for(val in x){

    if(i == 1){
      ret <- 0 #first monthly return is 0
      sol <- c(sol, ret)
    }

    #calc the return and append to list
    ret <- (x[i]-x[i-1])/x[i-1]
    sol <- c(sol, ret)

    #increase index
    i <- i+1

  }

  #return the solution
  return(sol)

}

#define a function to annualize a vector of monthly returns
aret <- function(x) {

  ra <- 1
  i <- 1
  for (val in x){
    ra <- ra*(1+x[i])
    i <- i+1 #NOTE! don't forget to increment!
  }

  ra <- ra - 1

  return(ra)

}

#calculate and print the value
x <- seq(100,112)
x <- mret(x)
print(x)

#annualize the monthly return and print
y <- x
y <- aret(y)
print(y)

#compare to the sum
print(sum(x))

#compare the average monthly return vs average of the monthly returns
z <- seq(1,12)
print(z/12)
print(mean(x))

#expected value of x
print(2*0.4*0.2*0.6*0.2+3*0.2*0.6*0.4*0.2*0.4*0.4+2*0.6*0.2*0.2*0.4+1*0.6*0.4)

#var(x|y=0)
x <- c(0.2,0.1,0.0,0.3)
print(var(x))
