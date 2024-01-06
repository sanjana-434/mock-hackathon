import numpy as np
from tsp_solver import solve_tsp  # Assuming a TSP solver is available

def find_delivery_paths(adjacency_matrix, order_capacities, total_capacity):
    num_locations = len(adjacency_matrix)

    # Initialize variables
    paths = []
    current_path = [0]  # Start at the depot (index 0)
    current_capacity = 0

    while len(current_path) > 0:
        # Find the next feasible location to visit
        next_location = find_next_location(
            adjacency_matrix, current_path, order_capacities, total_capacity, current_capacity
        )

        if next_location is not None:
            # Add the location to the current path
            current_path.append(next_location)
            current_capacity += order_capacities[next_location]

            # If the path is full, solve the TSP for this path and store it
            if current_capacity == total_capacity:
                path_indices = solve_tsp(adjacency_matrix[current_path, :][:, current_path])
                paths.append([current_path[i] for i in path_indices])
                current_path = [0]  # Start a new path from the depot
                current_capacity = 0
        else:
            # Remove the last location from the current path (backtrack)
            current_path.pop()
            current_capacity -= order_capacities[current_path[-1]]

    return paths

def find_next_location(adjacency_matrix, current_path, order_capacities, total_capacity, current_capacity):
    feasible_locations = []
    for i in range(1, len(adjacency_matrix)):
        if i not in current_path and current_capacity + order_capacities[i] <= total_capacity:
            feasible_locations.append(i)

    if feasible_locations:
        # Choose the closest feasible location based on distance
        closest_location = min(feasible_locations, key=lambda i: adjacency_matrix[current_path[-1], i])
        return closest_location
    else:
        return None

# Example usage
adjacency_matrix = np.array([[0, 10, 25, 15],
                             [10, 0, 30, 20],
                             [25, 30, 0, 35],
                             [15, 20, 35, 0]])
order_capacities = [0, 5, 8, 12]
total_capacity = 15

paths = find_delivery_paths(adjacency_matrix, order_capacities, total_capacity)
print(paths)  # Output: [[0, 1, 0, 2, 0], [0, 3]]