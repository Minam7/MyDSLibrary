import unittest
from collections import deque

from mylib.bellmanFord import bellman_ford
from mylib.dijkstra import dijkstra
from mylib.shortestPathDag import GraphWeighted, topological_sort, dag_shortest


class TestDAGShortest(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GraphWeighted()
        self.g.add_vertices([0, 1, 2, 3, 4, 5])

        self.g.add_edge(0, 1, 5)
        self.g.add_edge(0, 2, 3)
        self.g.add_edge(1, 3, 6)
        self.g.add_edge(1, 2, 2)
        self.g.add_edge(2, 4, 4)
        self.g.add_edge(2, 5, 2)
        self.g.add_edge(2, 3, 7)
        self.g.add_edge(3, 4, -1)
        self.g.add_edge(4, 5, -2)

    def test_topological_sort(self):
        res = topological_sort(self.g, 1)

        answer_parent = {1: None, 2: 1, 3: 1, 4: 3, 5: 4}
        self.assertEqual(answer_parent, res.parent)

        answer_order = deque([5, 4, 3, 2, 1])
        self.assertEqual(answer_order, res.order)

    def test_directed(self):
        answer = {0: float('inf'), 1: 0, 2: 2, 3: 6, 4: 5, 5: 3}
        dag_res = dag_shortest(self.g, 1)

        for node in dag_res:
            self.assertEqual(dag_res[node].cost, answer[node])

    def test_none_case(self):
        self.assertEqual(dag_shortest(None, 1), None)
        self.assertEqual(dag_shortest('w', None), None)
        self.assertEqual(dag_shortest(None, None), None)

    def test_one_node(self):
        g = GraphWeighted()
        g.add_vertices([0])
        self.assertEqual(dag_shortest(g, 0)[0].cost, 0)
        self.assertEqual(dag_shortest(g, 0)[0].pre_node, None)

    def test_not_in_node(self):
        with self.assertRaises(Exception) as context:
            dag_shortest(self.g, 'w')

        self.assertTrue('Source is not in the graph!' in str(context.exception))


class TestDijkstra(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GraphWeighted()
        self.g.add_vertices(['A', 'B', 'C', 'D', 'E'])

        self.g.add_edge('A', 'B', 10)
        self.g.add_edge('A', 'C', 3)
        self.g.add_edge('B', 'C', 1)
        self.g.add_edge('B', 'D', 2)
        self.g.add_edge('C', 'B', 4)
        self.g.add_edge('C', 'D', 8)
        self.g.add_edge('C', 'E', 2)
        self.g.add_edge('D', 'E', 7)
        self.g.add_edge('E', 'D', 9)

    def test_directed(self):
        answer = {'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}
        path_res = dijkstra(self.g, 'A')

        for node in path_res:
            self.assertEqual(path_res[node].cost, answer[node])

    def test_none_case(self):
        self.assertEqual(dijkstra(None, 1), None)
        self.assertEqual(dijkstra('w', None), None)
        self.assertEqual(dijkstra(None, None), None)

    def test_one_node(self):
        g = GraphWeighted()
        g.add_vertices([0])
        self.assertEqual(dijkstra(g, 0)[0].cost, 0)
        self.assertEqual(dijkstra(g, 0)[0].pre_node, None)

    def test_not_in_node(self):
        with self.assertRaises(Exception) as context:
            dijkstra(self.g, 'w')

        self.assertTrue('Source is not in the graph!' in str(context.exception))


class TestBellmanFord(unittest.TestCase):
    def setUp(self) -> None:
        self.g = GraphWeighted()
        self.g.add_vertices(['S', 'A', 'B', 'C', 'D', 'T'])

        self.g.add_edge('S', 'A', 5)
        self.g.add_edge('S', 'C', -2)
        self.g.add_edge('A', 'B', 1)
        self.g.add_edge('B', 'D', -1)
        self.g.add_edge('B', 'T', 3)
        self.g.add_edge('C', 'A', 2)
        self.g.add_edge('C', 'B', 4)
        self.g.add_edge('C', 'D', 4)
        self.g.add_edge('D', 'T', 1)

    def test_directed_cycle(self):
        path_res = bellman_ford(self.g, 'S')

        answer_cost = {'S': 0, 'A': 0, 'B': 1, 'C': -2, 'D': 0, 'T': 1}
        answer_parent = {'S': None, 'A': 'C', 'B': 'A', 'C': 'S', 'D': 'B', 'T': 'D'}

        for node in path_res:
            assert path_res[node].cost == answer_cost[node]
            assert path_res[node].pre_node == answer_parent[node]

    def test_negative_cycle(self):
        g = GraphWeighted()
        g.add_vertices(['S', 'A', 'B', 'C', 'D', 'T'])

        g.add_edge('S', 'A', 5)
        g.add_edge('S', 'C', -2)
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'D', -1)
        g.add_edge('B', 'T', 3)
        g.add_edge('B', 'C', -5)
        g.add_edge('C', 'A', 2)
        g.add_edge('C', 'D', 4)
        g.add_edge('D', 'T', 1)

        with self.assertRaises(Exception) as context:
            bellman_ford(g, 'S')

        self.assertTrue('Negative cycle detected!' in str(context.exception))

    def test_none_case(self):
        self.assertEqual(bellman_ford(None, 1), None)
        self.assertEqual(bellman_ford('w', None), None)
        self.assertEqual(bellman_ford(None, None), None)

    def test_one_node(self):
        g = GraphWeighted()
        g.add_vertices([0])
        self.assertEqual(bellman_ford(g, 0)[0].cost, 0)
        self.assertEqual(bellman_ford(g, 0)[0].pre_node, None)

    def test_not_in_node(self):
        with self.assertRaises(Exception) as context:
            bellman_ford(self.g, 'w')

        self.assertTrue('Source is not in the graph!' in str(context.exception))
