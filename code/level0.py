# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level0.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
for i in range(0,n):
    dist.append(data['neighbourhoods']['n'+str(i)]['distances'])

# for i in dist:
#     print(i)


path = []
def travellingsalesman(c):
    global cost
    adj_vertex = 99999
    min_val = 99999
    visited[c] = 1
    path.append((c + 1))
    for k in range(n):
        if (tsp_g[c][k] != 0) and (visited[k] == 0):
            if tsp_g[c][k] < min_val:
                min_val = tsp_g[c][k]
                adj_vertex = k
    if min_val != 99999:
        cost = cost + min_val
    if adj_vertex == 99999:
        adj_vertex = 0
        path.append(adj_vertex + 1)
        cost = cost + tsp_g[c][adj_vertex]
        return
    travellingsalesman(adj_vertex)
cost = 0
visited = np.zeros(n, dtype=int)
tsp_g = np.array(dist)
print("Shortest Path:", end=" ")
travellingsalesman(0)
print(path)
print("Minimum Cost:", end=" ")
print(cost)

f.close()


 
# Data to be written
# dictionary = {"v0": {"path": ["r0", "n0", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "r0"]}}
path_ = ['r'+str(path[0]-1)]
for i in path:
    path_.append('n'+str(i-1))

path_[-1]= 'r'+str(path[0]-1)
print(path_)
dictionary = {"v0": {"path": path_}}
print(dictionary)


# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("C:/work-shop/output/level0-output.json", "w") as outfile:
    outfile.write(json_object)
