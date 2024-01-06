
import math
from sys import maxsize 
from itertools import permutations
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

maxsize = float('inf')


def copyToFinal(curr_path):
	final_path[:N + 1] = curr_path[:]
	final_path[N] = curr_path[0]

def firstMin(adj, i):
	min = maxsize
	for k in range(N):
		if adj[i][k] < min and i != k:
			min = adj[i][k]

	return min
def secondMin(adj, i):
	first, second = maxsize, maxsize
	for j in range(N):
		if i == j:
			continue
		if adj[i][j] <= first:
			second = first
			first = adj[i][j]

		elif(adj[i][j] <= second and
			adj[i][j] != first):
			second = adj[i][j]

	return second

def TSPRec(adj, curr_bound, curr_weight, 
			level, curr_path, visited):
	global final_res

	if level == N:

		if adj[curr_path[level - 1]][curr_path[0]] != 0:

			curr_res = curr_weight + adj[curr_path[level - 1]]\
										[curr_path[0]]
			if curr_res < final_res:
				copyToFinal(curr_path)
				final_res = curr_res
		return
	for i in range(N):
	
		if (adj[curr_path[level-1]][i] != 0 and
							visited[i] == False):
			temp = curr_bound
			curr_weight += adj[curr_path[level - 1]][i]

			if level == 1:
				curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
								firstMin(adj, i)) / 2)
			else:
				curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
								firstMin(adj, i)) / 2)


			if curr_bound + curr_weight < final_res:
				curr_path[level] = i
				visited[i] = True
		
				TSPRec(adj, curr_bound, curr_weight, 
					level + 1, curr_path, visited)
			curr_weight -= adj[curr_path[level - 1]][i]
			curr_bound = temp
			visited = [False] * len(visited)
			for j in range(level):
				if curr_path[j] != -1:
					visited[curr_path[j]] = True

def TSP(adj):
	curr_bound = 0
	curr_path = [-1] * (N + 1)
	visited = [False] * N

	for i in range(N):
		curr_bound += (firstMin(adj, i) +
					secondMin(adj, i))

	curr_bound = math.ceil(curr_bound / 2)
	visited[0] = True
	curr_path[0] = 0

	TSPRec(adj, curr_bound, 0, 1, curr_path, visited)


adj = dist
N = n

final_path = [None] * (N + 1)

visited = [False] * N

final_res = maxsize
TSP(adj)

print("Minimum cost :", final_res)
print("Path Taken : ", end = ' ')
print(final_path)
for i in range(N + 1):
	print(final_path[i], end = ' ')

path = final_path
path_ = ['r0']
for i in path:
    path_.append('n'+str(i))
path_.pop()
path_.append('r0')
print(path_)
dictionary = {"v0": {"path": path_}}
print(dictionary)


# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("C:/work-shop/output/level0-output.json", "w") as outfile:
    outfile.write(json_object)



