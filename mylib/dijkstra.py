import heapq

from shortestPathDag import GraphWeighted, ShortestPathResult


def dijkstra(graph_in, source_in):
    if graph_in is None or source_in is None:
        return None

    if source_in not in graph_in.adj:
        raise ValueError('Source is not in the graph!')

    result = {v: ShortestPathResult(float('inf')) for v in graph_in.adj}

    result[source_in].cost = 0

    # add source as min distance
    priority_q = [(0, source_in)]

    while len(priority_q) > 0:
        (current_distance, min_node) = heapq.heappop(priority_q)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > result[min_node].cost:
            continue

        # update distances to adjacent nodes
        for (node, weight) in graph_in.adj[min_node]:
            new_dist = current_distance + weight

            if new_dist < result[node].cost:
                result[node].cost = new_dist
                result[node].pre_node = min_node
                heapq.heappush(priority_q, (new_dist, node))

    return result


if __name__ == '__main__':
    g = GraphWeighted()
    g.add_vertices(['A', 'B', 'C', 'D', 'E'])

    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 2)
    g.add_edge('C', 'B', 4)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 2)
    g.add_edge('D', 'E', 7)
    g.add_edge('E', 'D', 9)
    print(g.adj)

    answer = {'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}
    dag_res = dijkstra(g, 'A')
    for key, value in dag_res.items():
        print('Node:', key, 'Cost:', value.cost, 'Previous Node:', value.pre_node)
