# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level0.json')
 

data = json.load(f)

# n = data['n_neighbourhoods']
n = 10
dist = []
for i in range(0,10):
    dist.append(data['neighbourhoods']['n'+str(i)]['distances'][0:10])

for i in dist:
    print(i)
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
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(dist)
print("Shortest Path:", end=" ")
travellingsalesman(0)
print()
print("Minimum Cost:", end=" ")
print(cost)


f.close()