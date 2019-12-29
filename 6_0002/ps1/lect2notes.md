# Lecture 1

## Search Tree
* Each branch is a choice
* Complexity is related to number of nodes in the tree
* O(2^(2+1))
* Room for improvement, remove useless leaves/branches
  * Doesn't change complexity of computation

## Is optimization hopeless
* In theory yes, 
* In practice no, because of something called dynamic programming
* Richard Bellman invented dynamic programming to confuse the customer and keep his funding.

### Call tree
* It's bad enough do something once, but to do it many times is really wasteful
* Store the answer and look it up when you need it
  * A dictionary almost always works in constant time
* The trick behind dynamic programming is memoization 
  * Trade memory for run-time

### fastFib
* has memo, see lecture slides
  * hella faster

### Exceptions as a flow of control
* easier than try accept sort of thing, "at least for me"

### Memozation is not a magic bullet
* Optimal sub-structure
  * Problem can be broken down into smaller independent sub problems
* Overlapping sub-problems
  * These smaller problems must be repeated to make a memo useful.
Merge sort can be broken into smaller sub-problems, but does not have over-lapping sub-problems.

### Search tree
* Are we ever solving the same problem at two nodes?
* We could write a dynamic programming solution, but would see no run-time benefits. 
  * We never
