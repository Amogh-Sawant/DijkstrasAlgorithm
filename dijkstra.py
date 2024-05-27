from heapdict import heapdict
from collections import defaultdict

def shortest(n, edges):

    def sol(node):
        if node not in back: return [node]

        return sol(back[node]) + [node]

    neighbors = defaultdict(lambda: defaultdict())

    heap = heapdict()
    back = {}

    for u, v, dist in edges:
        neighbors[u][v] = dist
        neighbors[v][u] = dist

    heap[0] = 0
    visited = set()

    while bool(heap):

        best_node, best_dist = heap.popitem()
        visited.add(best_node)

        if best_node == n-1:
            path = sol(n-1)
            if path[0] != 0: return None
            return best_dist, path

        for neighbor in neighbors[best_node]:
            if neighbor not in visited: # not in blackened nodes
                if neighbor in heap:
                    if best_dist + neighbors[best_node][neighbor] <= heap[neighbor]:
                        heap[neighbor] = best_dist + neighbors[best_node][neighbor]
                        back[neighbor] = best_node
                else:
                    heap[neighbor] = best_dist + neighbors[best_node][neighbor]
                    back[neighbor] = best_node


x = shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])

print(x)