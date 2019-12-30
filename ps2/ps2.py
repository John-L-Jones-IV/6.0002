#!/usr/bin/env python3
# 6.0002 Problem Set 5
# Graph optimization
# Name: <John-L-Jones-IV>
# Collaborators: <tuhang102>
# Time: ~5 hrs

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge
from copy import deepcopy

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer: Nodes represent buildings. Edges paths between two buildings. 
# Weights represent distances between the two buildings.
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    with open(map_filename) as f:
        print("Loading map from file...")
        read_data = f.read()
    f.close()
    read_data = read_data.split()

    g = Digraph()
    for i in range (0, len(read_data), 4):
        node_source = Node(read_data[i])
        node_destination = Node(read_data[i+1])
        total_distance = read_data[i+2]
        outside_distance = read_data[i+3]
        edge = WeightedEdge(node_source, node_destination, total_distance, outside_distance)
        # ensure nodes are in Digraph
        if not g.has_node(node_source):
            g.add_node(node_source)
        if not g.has_node(node_destination):
            g.add_node(node_destination)
        # add edge to Digraph
        g.add_edge(edge)

    return g
    

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer: obtain shortest total distance between two nodes by 
# traversing edges, while not exceeding the outdoor distance limit
# Learning Experience: the list method .copy() does create a element by element copy of the list
# however; if one element of the list is a refernce object, such as another list that reference object is 
# only a shallow copy. Therfore the deepcopy() method from the copy library is used to copy all elements of the
# path list.
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    if not digraph.has_node(start) or not digraph.has_node(start):
        raise ValueError('Invalid node')
    path_cpy = deepcopy(path)
    path_cpy[0].append(start.get_name())
    if start == end:
        return (path_cpy[0].copy(), path_cpy[1])
    start_total_dist = path_cpy[1]
    start_outdoor_dist = path_cpy[2]
    for edge in digraph.get_edges_for_node(start): 
        if edge.get_destination().get_name() not in path_cpy[0]:
            path_cpy[1] = start_total_dist + int(edge.get_total_distance())
            path_cpy[2] = start_outdoor_dist + int(edge.get_outdoor_distance())
            if path_cpy[2] > max_dist_outdoors or path_cpy[1] > best_dist:
                continue
            new_path = get_best_path(digraph, edge.get_destination(), end, deepcopy(path_cpy),\
                max_dist_outdoors, best_dist, best_path.copy())
            if new_path[1] < best_dist:
                  best_path = new_path[0].copy()
                  best_dist = new_path[1]

    return (best_path.copy(), best_dist)

# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    LARGE = 2**30
    path = get_best_path(digraph, Node(start), Node(end), [[],0,0], max_dist_outdoors, LARGE, [])
    if path[1] > max_total_dist:
      raise ValueError('No path satisfies max_total_dist')
    if path[1] is None:
      raise ValueError('No path satisfies max_total_dist and max_dist_outdoors')
    return path[0]

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)

    def test1(self):
        self._test_path(expectedPath=['1','3'])

    def test2(self):
        self._test_path(expectedPath=['1','5','7'])

    def test3(self):
        self._test_path(expectedPath=['50','14','2'])

if __name__ == "__main__":
  #    digraph =  load_map('test_load_map.txt')
  #    start = Node('a')
  #    end = Node('c')
  #    max_total_dist = 90
  #    max_dist_outdoors = 60
  #    print(directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors))
    unittest.main()
