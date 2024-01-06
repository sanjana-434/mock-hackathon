# code by Sanjana R (21pd31)

import json
import numpy as np
 
f = open('C:/work-shop/Inputdata/level1a.json')
 

data = json.load(f)

n = data['n_neighbourhoods']

dist = []
dist.append([0])
res = data['restaurants']['r0']['neighbourhood_distance']
dist[0].extend(res)
for i in range(0,n):
    dist.append([res[i]])
    dist[i+1].extend(data['neighbourhoods']['n'+str(i)]['distances'])


# for i in dist:
#     print(i)
order_quantity = []
for i in range(0,n):
    order_quantity.append(data['neighbourhoods']['n'+str(i)]['order_quantity'])
# print(order_quantity)
# print(sum(order_quantity))

capacity = data['vehicles']['v0']['capacity']
# print(capacity)

import numpy as np

def greedy(node,graph,order,cap,vis,c,path):
    while(True):
        dict_ = {}
        idx = 0
        # print(graph[node])
        for j in graph[node]:
            dict_[j] = idx
            idx+=1
        
        myKeys = list(dict_.keys())
        myKeys.sort()
        dict_ = {i: dict_[i] for i in myKeys}

        flag = 0
        for key, value in dict_.items():
            if (key!=value):
                if (vis[value-1]==0 and c+order[value-1] <= cap):
                    flag = 1
                    vis[value-1] = 1
                    path.append(value)
                    c += order[value-1]
        if (flag == 0):
            break
        node = value
    return path


adjacency_matrix = np.array([
    [0, 2, 4, 1, 3],
    [2, 0, 5, 2, 1],
    [4, 5, 0, 3, 2],
    [1, 2, 3, 0, 4],
    [3, 1, 2, 4, 0]
])

order_quantity = [3, 2, 2, 3]
vis = []
for i in range(0,len(order_quantity)):
    vis.append(0)
capacities = 6
while(len(adjacency_matrix) != 1):
    path = greedy(0,adjacency_matrix,order_quantity,capacities,vis,0,[])
    for i in path:
        adjacency_matrix = np.delete(adjacency_matrix, i, axis=0) 
        adjacency_matrix = np.delete(adjacency_matrix, i, axis=1)
        order_quantity.pop(i-1)
        vis.pop(i-1)
    print(path)

