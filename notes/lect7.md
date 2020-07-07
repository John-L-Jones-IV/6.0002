# Lecture 7: Confidence Intervals
Emperical rule. ~95% of the data will fall within two standard deviations of a set of data 
that has a normal gaussian distribution.

In python these are easy to create with the random.gauss function.
This is a built in function of the random library. 
This has the arguments u and sigma

pylab.hist creates a histogram. 
Normally when we create a histogram we take all the values from min to max
and create a discrete number of bins.
Each value is weighted by 1. However, this can chage with the weight argument in
pylab.hist(weigth= ...)

scipy.intergrate.quad() integral aprox. Using a numberical technique.

If we used the sum of many random variables, we can use the Central Limit Theorem.
For example: a single dice roll is equally and evenly distributed.
However, the sum of many rolls of the dice is a normal distribution with a mean 
around 3.5.


