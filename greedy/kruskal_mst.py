import sys
sys.path.append("..")

from dataStrucutures import disjoint_set


def kruskal_mst(weighted_edges, total_nodes):
    nodes = [0] * (total_nodes + 1)

    print(len(nodes))
    for node_label in range(1, total_nodes + 1):
        nodes[node_label] = disjoint_set.make_set(node_label)

    weighted_edges.sort(key=lambda x: x[2])

    index = 0
    mst = []
    while len(mst) != (total_nodes - 1) and index < len(weighted_edges):
        current_edge = weighted_edges[index]

        if disjoint_set.find_set(nodes[current_edge[0]]) != disjoint_set.find_set(nodes[current_edge[1]]):
            mst.append(current_edge)
            disjoint_set.union(nodes[current_edge[0]], nodes[current_edge[1]])
        index += 1

    return mst


weighted_edges = [[1, 2, 4], [1, 3, 8], [2, 3, 9], [2, 4, 8], [3, 4, 2], [2, 5, 10], [3, 6, 1], [4, 5, 7], [4, 6, 9],
                  [5, 6, 5], [5, 7, 6], [6, 7, 2]]
total_nodes = 7
mst = kruskal_mst(weighted_edges, total_nodes)

print("MST :", mst)
mst_w = [e[2] for e in mst]
print("MST weight is ", sum(mst_w))
