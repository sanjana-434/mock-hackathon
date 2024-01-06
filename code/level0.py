# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level0.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
dist.append([0])
res = data['restaurants']['r0']['neighbourhood_distance']
dist[0].extend(res)
for i in range(0,n):
    dist.append([res[i]])
    dist[i+1].extend(data['neighbourhoods']['n'+str(i)]['distances'])

n+=1
for i in dist:
    print(i)


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
for i in range(0,len(path)):
    path[i]-=1

f.close()


 
# Data to be written
# dictionary = {"v0": {"path": ["r0", "n0", "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9", "r0"]}}
path_ = []
path_.append('r0')
for i in range(1,len(path)-1):
    path_.append('n'+str(path[i]-1))
path_.append('r0')
print(path_)
dictionary = {"v0": {"path": path_}}
print(dictionary)


# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("C:/work-shop/output/level0-output.json", "w") as outfile:
    outfile.write(json_object)
