Some information about the series.

Exo 1

In the previous course, you saw some method to smooth a time series by taking a average over a give time (lag). The purpose of these method are to remove the non-significant variation on the line but keeping the interesting variation of the line.

For example, the most extreme method would be to take the average over the whole time series, but in this case we would have a flat line. So with this method all the irregularity are removed, but we lose all the information on the underlying process.

So you have the implement the moving average (MA) and the exponential moving average (EMA) and play with the parameters to understand the methods.

In this exercise, as we generate random number, it’s good the set the seed of the random number generator. So if you use a other language, you have to replace the “set.seed(0)”, by the corresponding function.

Exo 2

You saw an algorithm to compute the number of directional change. In this algorithm there is a parameters delta that gives the length of the change that need to be reach in order to be counted.

For the data, the best is to use the mid price, so you have to compute it.
