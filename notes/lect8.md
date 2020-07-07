# Lecture 8. Sampling and Standard Error
Differential statisics.
Make observations on the population by taking random samples from the population.

Confidence intervals. Can give us bounds on our estimation from the samples.
Note these are statisical bounds, still vunerable to bugs and errors. And 
should not be mistaken as ground truth.

Think about political polls. These are not taken from simulations.
They claim to have a confidence interval (usually large).

Simple random sampling: each member of the population has equal chance
of being in the sample.

Stratified sampling. Seprate into subgroups and sample from the subgroups.
Each group is represented proportionally to the size of the group.
This is the way most political polls are done.

## Data Science
Most of the material from this point on in the class will be 
an introduction to data science.

Usually we do sampling without replacement, meaning we will not take the
same item from the popluation multiple times in the sample.

If we draw samples should we expect the characteristics of the sample mirror
the characterstics of the population? Sometimes yes. Sometimes no.
In general, if the sample size is large enough, the sample *should* reflect
the chacteristics of the population.

If we want a tighter bound what can we do?
* More samples
	* Doing it more often is not going to help.
* Larger samples
	* Increasing the size of the samples does cause the std dev to drop.

How can we visualize this?
Error bar. Shows confidence intervals overlapping between sample groups.

As the sample size increases the standard deviation gets smaller, i.e. more confidence.

### Recall the Central Limit Theorem
1. The means of the samples in a set of samples (the sample means) will be approximately
normally distributed
2. This normal distribution will have a mean close to the mean population
3. The variance of the sample means will be close to the variance of the population
devided by the sample size.

### It's time to use the 3rd feature.
Computed standared error of the mean SEM or SE

SE = rho/sqrt(n)
Where rho is the population standard deviation and n is the size of the sample.
What is the relationship between the standard deviation to the standard error?

Here's the catch. We don't know rho: the standard deviation of the population.
What's our best guess? The standard deviation of the samples.
Well it seems to work... good enough I guess...
If the sample size is larger, this is an even better guess.

If the sample size is large enough, the sample std dev ~= pop std dev

### Is this limited to our dataset on temperatures?
Observe distributions:
1. Uniform
2. Normal
3. Exponential

There are different results dependent on the skew of these distributions.
If the distribution is very asymetric you need more samples. 
Does size matter? Shockingly no. If you have a bigger population, you don't need
more samples.
This is why political polls are shockingly small.
To estimate the mean of a population given a single sample, we based our required 
sample size on the skew of the distribution.
Well aren't political polls very skewed?
Use sample rho to estimate SE.
Used estimated SE to generate confidence intervals around the mean.
Must choose independant samples. Which in political polls is not the actual truth.


Note: 5% of our sample data should be outside of our 95% confidence interval.
"If you called every election correctly, then your math is wrong."
