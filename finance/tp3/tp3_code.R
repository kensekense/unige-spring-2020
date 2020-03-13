#we can define col.names in our table reads
tab <- read.table("C:/Users/liveo/Desktop/playground/unige-spring-2020/finance/tp3/EUR_USD-20120101-20120301.dat", col.names=c("timestamp","bid","ask"))

#we can convert to POSIXct with as.POSIXct(tab$timestamp, origin = "1970-01-01")
tab$timestamp = as.POSIXct(tab$timestamp, origin="1970-01-01")

#we can use breaks, trunc and add labels such as "hours"
seg <- trunc(range(tab$timestamp), "hours")

#we can use sequences and use by = "15 min" which is recognized by R
breaks <- seq(seg[1], seg[2]+3600, by="15min")

#histogram
hist(tab$timestamp, breaks=breaks, main="EUR_USD Daily Distribution")
