
import json
import numpy as np
import sys
 
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



V = n
answer = []

def tsp(graph, v, currPos, n, count, cost):
 
    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return
 
    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
            v[i] = True
            tsp(graph, v, i, n, count + 1, 
                cost + graph[currPos][i])

            v[i] = False
 
graph= dist

v = [False for i in range(n)]
    
v[0] = True

tsp(graph, v, 0, n, 1, 0)

print((answer))