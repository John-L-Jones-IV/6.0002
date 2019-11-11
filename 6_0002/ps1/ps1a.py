#!/usr/bin/env python3
###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: <John-L-Jones-IV>
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
  """
  Read the contents of the given file.  Assumes the file contents contain
  data in the form of comma-separated cow name, weight pairs, and return a
  dictionary containing cow names as keys and corresponding weights as values.

  Parameters:
  filename - the name of the data file as a string

  Returns:
  a dictionary of cow name (string), weight (int) pairs
  """
  f = open(filename,'r')
  txt = f.read()
  f.close()

  L = txt.replace('\n',',').split(',')
  d = {}
  for i in range(0, len(L)-1, 2):
    d[L[i]] = int(L[i+1])

  return d

# Problem 2
def greedy_cow_transport(cows,limit=10):
  """
  Uses a greedy heuristic to determine an allocation of cows that attempts to
  minimize the number of spaceship trips needed to transport all the cows. The
  returned allocation of cows may or may not be optimal.
  The greedy heuristic should follow the following method:

  1. As long as the current trip can fit another cow, add the largest cow that will fit
      to the trip
  2. Once the trip is full, begin a new trip to transport the remaining cows

  Does not mutate the given dictionary of cows.

  Parameters:
  cows - a dictionary of name (string), weight (int) pairs
  limit - weight limit of the spaceship (an int)
  
  Returns:
  A list of lists, with each inner list containing the names of cows
  transported on a particular trip and the overall list containing all the
  trips
  """
  cows_cpy = sorted(cows.copy(), key=cows.get, reverse=True)
  for cow in cows:
    if cows[cow] > limit:
      cows_cpy.remove(cow)
  L = []
  while len(cows_cpy):
    payload = 0
    cows_aboard = []
    for cow in cows_cpy[:]:
      if cows[cow] + payload <= limit:
        cows_aboard.append(cow)
        payload += cows.get(cow)
        cows_cpy.remove(cow)
    L.append(cows_aboard[:])

  return L

# Problem 3
def brute_force_cow_transport(cows,limit=10):
  """
  Finds the allocation of cows that minimizes the number of spaceship trips
  via brute force.  The brute force algorithm should follow the following method:

  1. Enumerate all possible ways that the cows can be divided into separate trips 
      Use the given get_partitions function in ps1_partition.py to help you!
  2. Select the allocation that minimizes the number of trips without making any trip
      that does not obey the weight limitation
          
  Does not mutate the given dictionary of cows.

  Parameters:
  cows - a dictionary of name (string), weight (int) pairs
  limit - weight limit of the spaceship (an int)
  
  Returns:
  A list of lists, with each inner list containing the names of cows
  transported on a particular trip and the overall list containing all the
  trips
  """
  cows_cpy = cows.copy()
  for cow in cows:
    if cows_cpy.get(cow) > limit:
      del cows_cpy[cow]
  partitions = get_partitions(cows_cpy)
  for partition in partitions:
    print(partition)
    for L in partition:
      for e in L:
        Sum += cows.get(e)
      print(Sum)

      
# Problem 4
def compare_cow_transport_algorithms():
  """
  Using the data from ps1_cow_data.txt and the specified weight limit, run your
  greedy_cow_transport and brute_force_cow_transport functions here. Use the
  default weight limits of 10 for both greedy_cow_transport and
  brute_force_cow_transport.
  
  Print out the number of trips returned by each method, and how long each
  method takes to run in seconds.

  Returns:
  Does not return anything.
  """
  # TODO: Your code here
  pass

if __name__ == '__main__':
  cows = {'A':1, 'B':2, 'C':3}
  brute_force_cow_transport(cows)

  #  cows = {'A':1, 'B':2, 'C':3}
  #  partitions = get_partitions(cows)
  #  for partition in partitions:
  #    print(partition)
  #    print(len(partition))
  #    for L in partition:
  #      for cow in L:
  #        print(cow)
  #      print('--')
