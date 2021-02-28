from collections import deque


class GraphWeighted:
    def __init__(self):
        self.adj = {}

    def add_vertices(self, list_in):
        for item in list_in:
            self.adj[item] = []

    def add_edge(self, u_in, v_in, w_in):
        self.adj[u_in].append((v_in, w_in))


class TopologicalSortResult:
    def __init__(self):
        self.parent = {}
        self.order = deque()


def topological_sort(graph_in, source_in, result_in=None):
    if source_in is None:
        return

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    if result_in is None:
        # first time DFS
        result_in = TopologicalSortResult()
        result_in.parent[source_in] = None

    for (node, _) in graph_in.adj[source_in]:
        if node not in result_in.parent:
            # unvisited node
            topological_sort(graph_in, node, result_in)
            result_in.parent[node] = source_in

    result_in.order.append(source_in)

    return result_in


class ShortestPathResult:
    def __init__(self, cost_in, pre_node_in=None):
        self.pre_node = pre_node_in
        self.cost = cost_in


def shortest_path_checker(graph_in, source_in, trajectory_in):
    for (node, weight) in graph_in.adj[source_in]:
        if node not in trajectory_in:
            # the first time we see this node
            # current distance to this node is INF
            trajectory_in[node] = ShortestPathResult(trajectory_in[source_in].cost + weight, source_in)

        else:
            # change it if we find a shorter route
            if trajectory_in[node].cost > (trajectory_in[source_in].cost + weight):
                trajectory_in[node].cost = trajectory_in[source_in].cost + weight
                trajectory_in[node].pre_node = source_in


def dag_shortest(graph_in, source_in):
    if graph_in is None or source_in is None:
        return None

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    topological_order = topological_sort(graph_in, source_in).order

    trajectory = {source_in: ShortestPathResult(0)}
    # add source with distance 0

    while topological_order:
        shortest_path_checker(graph_in, topological_order.pop(), trajectory)

    # add nodes that are no path to them as INF
    for node in graph_in.adj:
        if node not in trajectory:
            trajectory[node] = ShortestPathResult(float('inf'))

    return trajectory


if __name__ == '__main__':
    g = GraphWeighted()
    g.add_vertices([0, 1, 2, 3, 4, 5])

    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 6)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, -1)
    g.add_edge(4, 5, -2)

    print(g.adj)
    # source = 1
    res = topological_sort(g, 1)
    print(res.parent)
    print(res.order)
    answer = {0: float('inf'), 1: 0, 2: 2, 3: 6, 4: 5, 5: 3}

    dag_res = dag_shortest(g, 1)
    for key, value in dag_res.items():
        print('Node:', key, 'Cost:', value.cost, 'Previous Node:', value.pre_node)
