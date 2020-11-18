def relax(u, v, w, d_arr):
    if d_arr[u] + w < d_arr[v] :
        d_arr[v] = d_arr[u] + w

def dijkstra(weighted_edges, start_node, n):
    """

    :param edges: A list of edges where each edge is represented by pairs of nodes that produce it
    """

    adj_array = [[] for _ in range(n + 1)]  # because of 1 based indexing
    d_arr = [ 9999 for _ in range(n + 1) ]

    for edge in weighted_edges:
        adj_array[edge[0]].append([edge[1], edge[2]])

    A = []
    A.append(start_node)
    cur_node = start_node
    d_arr[start_node] = 0
    unexplored_set = {i for i in range(1,n+1)}
    unexplored_set.remove(cur_node)

    while len(unexplored_set) != 0 :
        for node in adj_array[cur_node]:
            relax(cur_node, node[0], node[1], d_arr)

        min_val = 9999
        min_index = None

        for node in unexplored_set:
            if d_arr[node] < min_val:
                min_val = d_arr[node]
                min_index = node


        A.append(min_index)
        cur_node = min_index
        unexplored_set.remove(cur_node)

    return A, d_arr

weighted_edges = [[1,2,10], [1,5,5], [2,3,1], [2,5,2], [3,4,4], [4,3,6], [4,1,7], [5,4,2], [5,3,9], [5,1,3] ]
total_nodes = 5
path, distances = dijkstra(weighted_edges, 1, total_nodes)

print("The order in which the edges are added : ", path)
print("distances from start node : ", distances[1:])







