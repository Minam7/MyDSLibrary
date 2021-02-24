from collections import deque
from enum import Enum


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertices(self, list_in):
        for item in list_in:
            self.adj[item] = []

    def add_edge(self, u_in, v_in):
        self.adj[u_in].append(v_in)


class Edge(Enum):
    TREE_EDGE = 'Tree Edge'
    BACKWARD_EDGE = 'Backward Edge'
    FORWARD_EDGE = 'Forward Edge'
    CROSS_EDGE = 'Cross Edge'


class BSFResult:
    def __init__(self):
        self.level = {}  # node: level
        self.parent = {}  # node: parent


def bfs(graph_in, source_in):
    """Queue-based implementation of BFS.
    Args:
    graph_in: a graph with adjacency list adj such that g.adj[u] is a list of u’s
    neighbors.
    source_in: source.
    """
    if graph_in is None or source_in is None:
        return

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    result = BSFResult()
    result.level[source_in] = 0
    result.parent[source_in] = None

    node_q = deque()
    node_q.append(source_in)

    while node_q:
        # while node_q is not empty
        walker = node_q.popleft()

        for item in graph_in.adj[walker]:
            if item not in result.level:
                # we haven't seen this item yet!
                result.level[item] = result.level[walker] + 1
                result.parent[item] = walker
                node_q.append(item)

    return result


class DFSResult:
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.time = 0


class DFSEdgeClassifierResult(DFSResult):
    def __init__(self):
        super().__init__()
        self.edges = {}  # edge classification
        self.order = []


def dfs(graph_in, source_in, result_in=None):
    if graph_in is None or source_in is None:
        return

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    if result_in is None:
        result_in = DFSResult()
        # initialize for source node
        result_in.parent[source_in] = None
        result_in.start_time[source_in] = result_in.time
        result_in.time += 1

    for item in graph_in.adj[source_in]:
        if item not in result_in.parent:
            # discovery event
            result_in.parent[item] = source_in
            result_in.start_time[item] = result_in.time
            result_in.time += 1
            dfs(graph_in, item, result_in)

    # finishing time
    result_in.finish_time[source_in] = result_in.time
    result_in.time += 1

    return result_in


def dfs_edge_visit_tagger(graph_in, source_in, result_in, parent_in=None):
    # initialize for source node
    result_in.parent[source_in] = parent_in
    result_in.start_time[source_in] = result_in.time
    result_in.time += 1

    if parent_in is not None:
        # we are looking at tree edges
        result_in.edges[(parent_in, source_in)] = Edge.TREE_EDGE

    for item in graph_in.adj[source_in]:
        if item not in result_in.parent:
            # discovery event
            dfs_edge_visit_tagger(graph_in, item, result_in, source_in)

        elif item not in result_in.finish_time:
            # we are looking at backward edges
            result_in.edges[(source_in, item)] = Edge.BACKWARD_EDGE

        elif result_in.start_time[item] > result_in.start_time[source_in]:
            # finished node
            result_in.edges[(source_in, item)] = Edge.FORWARD_EDGE
        else:
            # finished node but different start time
            result_in.edges[(source_in, item)] = Edge.CROSS_EDGE

    # finishing time
    result_in.finish_time[source_in] = result_in.time
    result_in.time += 1
    result_in.order.append(source_in)

    return result_in


def dfs_edge_classifier(graph_in):
    if graph_in is None:
        return

    result = DFSEdgeClassifierResult()

    for vertex in graph_in.adj.keys():
        if vertex not in result.parent:
            dfs_edge_visit_tagger(graph_in, vertex, result)

    return result


def topological_sort(graph_in):
    if graph_in is None:
        return

    resulted = dfs_edge_classifier(graph_in)
    resulted.order.reverse()
    return resulted.order
