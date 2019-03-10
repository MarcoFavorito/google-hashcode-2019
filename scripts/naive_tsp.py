import itertools

import numpy as np

"""
Naive implementation of the Held-Karp algorithm.
https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
"""


if __name__ == '__main__':
    graph = np.asarray([
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ])

    all_nodes = set(range(4))
    start = 0
    nodes = all_nodes.difference({start})

    C = {}

    for i in nodes:
        C[(i, frozenset())] = graph[(i, start)]

    for k in range(1, len(nodes)):
        combs = list(itertools.combinations(nodes, k))
        for c in combs:
            cur_set = frozenset(c)
            cur_nodes = nodes.difference(cur_set)
            for i in cur_nodes:
                C[(i, cur_set)] = min([graph[i, prev] + C[prev, frozenset(c).difference({prev})] for prev in c])

    # reconstruct the path
    previous_nodes = set(nodes)
    path = [start]
    current_node = start
    while len(previous_nodes) != 0:
        current_node = min(previous_nodes, key=lambda x: graph[current_node, x] + C[(x, frozenset(previous_nodes).difference({x}))])
        path.append(current_node)
        previous_nodes.remove(current_node)

    path.append(start)
    assert path == [0, 2, 3, 1, 0]
    print(path)


