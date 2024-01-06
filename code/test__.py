import numpy as np
import json
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

def nearest_neighbor_algorithm(adjacency_matrix):
    n = len(adjacency_matrix)
    visited = [False] * n
    tour = [0]  # Start from the first city

    for _ in range(1, n):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None

        for i in range(n):
            if not visited[i] and i != current_city and adjacency_matrix[current_city][i] < min_distance:
                min_distance = adjacency_matrix[current_city][i]
                nearest_city = i

        tour.append(nearest_city)
        visited[nearest_city] = True

    tour.append(tour[0])  # Return to the starting city to complete the tour
    total_distance = sum(adjacency_matrix[tour[i]][tour[i + 1]] for i in range(n))

    return tour, total_distance

if __name__ == "__main__":
    # Example: Adjacency matrix representing distances between cities
    adjacency_matrix = np.array(dist)

    # Applying the Nearest Neighbor Algorithm
    tour, total_distance = nearest_neighbor_algorithm(adjacency_matrix)

    # Output the result with the shortest path
    print(tour)

    print("Shortest Path:", path_str)
    print("Total Distance:", total_distance)
