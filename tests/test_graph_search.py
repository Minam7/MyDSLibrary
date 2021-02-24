import unittest

from mylib.graphSearch import *


class TestBFS(unittest.TestCase):
    def test_correct_directed(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c', 'd', 'e', 'f'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('a', 'e')
        g_test.add_edge('a', 'f')
        g_test.add_edge('b', 'd')
        g_test.add_edge('c', 'b')
        g_test.add_edge('d', 'c')
        g_test.add_edge('d', 'e')

        answer_level = {'a': 0, 'b': 1, 'c': 3, 'd': 2, 'e': 1, 'f': 1}
        test_result = bfs(g_test, 'a')
        self.assertEqual(answer_level, test_result.level)

        answer_parent = {'a': None, 'b': 'a', 'c': 'd', 'd': 'b', 'e': 'a', 'f': 'a'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_correct_undirected(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c', 'd'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('a', 'd')
        g_test.add_edge('b', 'a')
        g_test.add_edge('b', 'c')
        g_test.add_edge('c', 'b')
        g_test.add_edge('c', 'd')
        g_test.add_edge('d', 'a')
        g_test.add_edge('d', 'c')

        answer_level = {'a': 1, 'b': 0, 'c': 1, 'd': 2}
        test_result = bfs(g_test, 'b')
        self.assertEqual(answer_level, test_result.level)

        answer_parent = {'a': 'b', 'b': None, 'c': 'b', 'd': 'a'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_no_cycle(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('b', 'c')

        answer_level = {'a': 0, 'b': 1, 'c': 2}
        test_result = bfs(g_test, 'a')
        self.assertEqual(answer_level, test_result.level)

        answer_parent = {'a': None, 'b': 'a', 'c': 'b'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_single_node(self):
        g_test = Graph()
        g_test.add_vertices(['a'])

        answer_level = {'a': 0}
        test_result = bfs(g_test, 'a')
        self.assertEqual(answer_level, test_result.level)

        answer_parent = {'a': None}
        self.assertEqual(answer_parent, test_result.parent)

    def test_not_in_graph_source(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('b', 'c')

        with self.assertRaises(Exception) as context:
            bfs(g_test, 'w')

        self.assertTrue('Source is not in the graph!' in str(context.exception))

    def test_none_case(self):
        self.assertEqual(bfs(None, 'w'), None)
        self.assertEqual(bfs(Graph(), None), None)


class TestDFS(unittest.TestCase):
    def test_correct_directed(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c', 'd', 'e', 'f'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('a', 'e')
        g_test.add_edge('a', 'f')
        g_test.add_edge('b', 'd')
        g_test.add_edge('c', 'b')
        g_test.add_edge('d', 'c')
        g_test.add_edge('d', 'e')

        test_result = dfs(g_test, 'a')

        answer_start = {'a': 0, 'b': 1, 'c': 3, 'd': 2, 'e': 5, 'f': 9}
        self.assertEqual(answer_start, test_result.start_time)

        answer_finish = {'a': 11, 'b': 8, 'c': 4, 'd': 7, 'e': 6, 'f': 10}
        self.assertEqual(answer_finish, test_result.finish_time)

        answer_parent = {'a': None, 'b': 'a', 'c': 'd', 'd': 'b', 'e': 'd', 'f': 'a'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_correct_undirected(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c', 'd'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('a', 'd')
        g_test.add_edge('b', 'a')
        g_test.add_edge('b', 'c')
        g_test.add_edge('c', 'b')
        g_test.add_edge('c', 'd')
        g_test.add_edge('d', 'a')
        g_test.add_edge('d', 'c')

        test_result = dfs(g_test, 'b')

        answer_start = {'a': 1, 'b': 0, 'c': 3, 'd': 2}
        self.assertEqual(answer_start, test_result.start_time)

        answer_finish = {'a': 6, 'b': 7, 'c': 4, 'd': 5}
        self.assertEqual(answer_finish, test_result.finish_time)

        answer_parent = {'a': 'b', 'b': None, 'c': 'd', 'd': 'a'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_no_cycle(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('b', 'c')

        test_result = dfs(g_test, 'a')

        answer_start = {'a': 0, 'b': 1, 'c': 2}
        self.assertEqual(answer_start, test_result.start_time)

        answer_finish = {'a': 5, 'b': 4, 'c': 3}
        self.assertEqual(answer_finish, test_result.finish_time)

        answer_parent = {'a': None, 'b': 'a', 'c': 'b'}
        self.assertEqual(answer_parent, test_result.parent)

    def test_single_node(self):
        g_test = Graph()
        g_test.add_vertices(['a'])

        test_result = dfs(g_test, 'a')
        answer_start = {'a': 0}
        self.assertEqual(answer_start, test_result.start_time)

        answer_finish = {'a': 1}
        self.assertEqual(answer_finish, test_result.finish_time)

        answer_parent = {'a': None}
        self.assertEqual(answer_parent, test_result.parent)

    def test_not_in_graph_source(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('b', 'c')

        with self.assertRaises(Exception) as context:
            dfs(g_test, 'w')

        self.assertTrue('Source is not in the graph!' in str(context.exception))

    def test_none_case(self):
        self.assertEqual(dfs(None, 'w'), None)
        self.assertEqual(dfs(Graph(), None), None)


class TestEdgeClassifierDFS(unittest.TestCase):
    def test_correct_directed(self):
        g_test = Graph()
        g_test.add_vertices(['a', 'b', 'c', 'd', 'e', 'f'])
        g_test.add_edge('a', 'b')
        g_test.add_edge('a', 'e')
        g_test.add_edge('a', 'f')
        g_test.add_edge('b', 'd')
        g_test.add_edge('c', 'b')
        g_test.add_edge('d', 'c')
        g_test.add_edge('d', 'e')
        g_test.add_edge('f', 'e')

        test_result = dfs_edge_classifier(g_test)
        self.assertEqual(test_result.edges[('a', 'b')], Edge.TREE_EDGE)
        self.assertEqual(test_result.edges[('b', 'd')], Edge.TREE_EDGE)
        self.assertEqual(test_result.edges[('d', 'c')], Edge.TREE_EDGE)
        self.assertEqual(test_result.edges[('d', 'e')], Edge.TREE_EDGE)
        self.assertEqual(test_result.edges[('a', 'f')], Edge.TREE_EDGE)
        self.assertEqual(test_result.edges[('c', 'b')], Edge.BACKWARD_EDGE)
        self.assertEqual(test_result.edges[('a', 'e')], Edge.FORWARD_EDGE)
        self.assertEqual(test_result.edges[('f', 'e')], Edge.CROSS_EDGE)

        self.assertEqual(test_result.order, ['c', 'e', 'd', 'b', 'f', 'a'])

    def test_single_node(self):
        g_test = Graph()
        g_test.add_vertices(['a'])

        test_result = dfs_edge_classifier(g_test)
        answer_start = {'a': 0}
        self.assertEqual(answer_start, test_result.start_time)

        answer_finish = {'a': 1}
        self.assertEqual(answer_finish, test_result.finish_time)

        answer_parent = {'a': None}
        self.assertEqual(answer_parent, test_result.parent)

        self.assertEqual(test_result.order, ['a'])

    def test_none_case(self):
        self.assertEqual(dfs_edge_classifier(None), None)
