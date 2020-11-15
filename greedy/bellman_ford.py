def relax(u, v, w, d_arr):
    if d_arr[u] + w < d_arr[v] :
        d_arr[v] = d_arr[u] + w

def bellman_ford(weighted_edges, start_node, n):
    """

    :param edges: A list of edges where each edge is represented by pairs of nodes that produce it
    """

    adj_array = [[] for _ in range(n + 1)]  # because of 1 based indexing
    d_arr = [ 9999 for _ in range(n + 1) ]
    d_arr[start_node] = 0

    for edge in weighted_edges:
        adj_array[edge[0]].append([edge[1], edge[2]])

    for i in range(1,n):    # run n-1 time
        for u,v,w in weighted_edges:
            relax(u, v ,w, d_arr)

    for u,v,w in weighted_edges:
        if d_arr[v] > d_arr[u] + w:
            return True, None

    return False, d_arr

weighted_edges = [[1,2,10], [1,5,5], [2,3,1], [2,5,2], [3,4,4], [4,3,6], [4,1,7], [5,4,2], [5,3,9], [5,1,3] ]
total_nodes = 5
has_negative_weight_cycle, distances = bellman_ford(weighted_edges, 1, total_nodes)

print("has_negative_weight_cycle? : ", has_negative_weight_cycle)
print("Distances: ", distances[1:])







