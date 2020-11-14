def prim_mst_naive(weighted_edges, n):
    """

    :param edges: A list of edges where each edge is represented by pairs of nodes that produce it
    """

    adj_array = [[] for _ in range(n + 1)]  # because of 1 based indexing

    for edge in weighted_edges:
        adj_array[edge[0]].append([edge[1], edge[2]])
        adj_array[edge[1]].append([edge[0], edge[2]])

    # Any node among [1, n] can be chosen as the starting node

    start_node = 1
    explored_set = {start_node}
    unexplored_set = set([i for i in range(2, n + 1)])

    solution = []
    for i in range(1, n):
        min_w = 9999
        node_pair = [None, None, None]
        for node in explored_set:
            adjacent_nodes = adj_array[node]
            for neighbour, weight in adjacent_nodes:
                if neighbour in unexplored_set:
                    if weight < min_w:
                        min_w = weight
                        node_pair = [node, neighbour, weight]
        solution.append(node_pair)
        explored_set.add(node_pair[1])
        unexplored_set.remove(node_pair[1])

    return solution


def prim_mst_mheap(weighted_edges, n):
    """

    :param weighted_edges:
    :param n:
    :return:
    """
    pass


weighted_edges = [[1, 2, 4], [1, 3, 8], [2, 3, 9], [2, 4, 8], [3, 4, 2], [2, 5, 10], [3, 6, 1], [4, 5, 7], [4, 6, 9],
                  [5, 6, 5], [5, 7, 6], [6, 7, 2]]
total_nodes = 7
mst = prim_mst_naive(weighted_edges, total_nodes)

print("MST :", mst)
mst_w = [e[2] for e in mst]
print("MST weight is ", sum(mst_w))
