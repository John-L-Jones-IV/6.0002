#!/usr/bin/env python3
import unittest
from ps1a import *
from ps1b import *

class TestCows(unittest.TestCase):
  def test_load_cows(self):
    varin = 'test1.txt'
    out = {'A':1,'B':2, 'C':3} 
    self.assertEqual(load_cows(varin), out)

    varin = 'test2.txt'
    out = {'Bob':109} 
    self.assertEqual(load_cows(varin), out)

    varin = 'test3.txt'
    out = {'Bob':5, 'Bill':1} 
    self.assertEqual(load_cows(varin), out)
    
    varin = 'ps1_cow_data.txt'
    out = {'Maggie':3,'Herman':7,'Betsy':9,'Oreo':6,'Moo Moo':3,'Milkshake':2,'Millie':5,'Lola':2,'Florence':2,'Henrietta':9}
    self.assertEqual(load_cows(varin), out)

    varin = 'ps1_cow_data_2.txt'
    out = {'Miss Moo-dy':3, 'Milkshake':4,'Lotus':10,'Miss Bella':2,'Horns':9,'Betsy':5,'Rose':3,'Dottie':6}
    self.assertEqual(load_cows(varin), out)

  def test_greedy_cow_transport(self):
    cows = {'Bob':9, 'Sally': 8, 'Billy':3, 'Fred':3, 'Josh':3}
    cows_cpy = cows.copy()
    L =[['Bob'],['Sally'],['Billy','Fred','Josh']]
    self.assertEqual(greedy_cow_transport(cows), L)
    self.assertEqual(cows,cows_cpy)

    cows = {'Bob':11, 'Sally': 8, 'Billy':3, 'Fred':3, 'Josh':3}
    cows_cpy = cows.copy()
    L =[['Sally'],['Billy','Fred','Josh']]
    self.assertEqual(greedy_cow_transport(cows), L)
    self.assertEqual(cows,cows_cpy)

    cows = {'A':1, 'B': 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
    cows_cpy = cows.copy()
    L =[['H','B'],['G','C'],['F','D'],['E','A']]
    self.assertEqual(greedy_cow_transport(cows), L)
    self.assertEqual(cows,cows_cpy)

    cows = {'A':12, 'B': 13}
    cows_cpy = cows.copy()
    L =[['A']]
    self.assertEqual(greedy_cow_transport(cows,limit = 12), L)
    self.assertEqual(cows,cows_cpy)
    
    cows = {'A':12, 'B': 11}
    cows_cpy = cows.copy()
    L =[['A'],['B']]
    self.assertEqual(greedy_cow_transport(cows,limit = 12), L)
    self.assertEqual(cows,cows_cpy)
