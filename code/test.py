import numpy as np
def travellingsalesman(c):
    global cost
    adj_vertex = 99999
    min_val = 99999
    visited[c] = 1
    print((c + 1), end=" ")
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 99999:
        cost = cost + min_val
    if adj_vertex == 99999:
        adj_vertex = 0
        print((adj_vertex + 1), end=" ")
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
n = 20
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array([[12, 30, 33, 10, 45],
                  [56, 22, 9, 15, 18],
                  [29, 13, 8, 5, 12],
                  [33, 28, 16, 10, 3],
                  [1, 4, 30, 24, 20]])
print("Shortest Path:", end=" ")
travellingsalesman(0)
print()
print("Minimum Cost:", end=" ")
print(cost)