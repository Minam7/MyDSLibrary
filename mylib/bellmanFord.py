from mylib.shortestPathDag import GraphWeighted, ShortestPathResult


def relax_all_edges(graph_in, result_in):
    changed = False
    for node in graph_in.adj:
        for (dest_node, weight) in graph_in.adj[node]:
            if result_in[node].cost + weight < result_in[dest_node].cost:
                result_in[dest_node].cost = result_in[node].cost + weight
                result_in[dest_node].pre_node = node
                changed = True

    return changed


def check_for_negative_cycle(graph_in, result_in):
    if relax_all_edges(graph_in, result_in) is True:
        raise ValueError('Negative cycle detected!')


def bellman_ford(graph_in, source_in):
    if graph_in is None or source_in is None:
        return None

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    result = {v: ShortestPathResult(float('inf')) for v in graph_in.adj}
    result[source_in].cost = 0
    result[source_in].pre_node = None

    for _ in range(len(graph_in.adj) - 1):
        is_relaxed = relax_all_edges(graph_in, result)
        if is_relaxed is False:
            break

    check_for_negative_cycle(graph_in, result)

    return result


if __name__ == '__main__':
    g = GraphWeighted()
    g.add_vertices(['S', 'A', 'B', 'C', 'D', 'T'])
    g.add_edge('S', 'A', 5)
    g.add_edge('S', 'C', -2)
    g.add_edge('A', 'B', 1)
    g.add_edge('B', 'D', -1)
    g.add_edge('B', 'T', 3)
    g.add_edge('C', 'A', 2)
    g.add_edge('C', 'B', 4)
    g.add_edge('C', 'D', 4)
    g.add_edge('D', 'T', 1)

    # Print the solution
    path_res = bellman_ford(g, 'S')

    for key, value in path_res.items():
        print('Node:', key, 'Cost:', value.cost, 'Previous Node:', value.pre_node)

    answer_cost = {'S': 0, 'A': 0, 'B': 1, 'C': -2, 'D': 0, 'T': 1}
    answer_parent = {'S': None, 'A': 'C', 'B': 'A', 'C': 'S', 'D': 'B', 'T': 'D'}

    for node in path_res:
        assert path_res[node].cost == answer_cost[node]
        assert path_res[node].pre_node == answer_parent[node]
