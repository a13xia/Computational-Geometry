import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

def compute_triangulation_and_visualize(lambda_value):
    # Define the points
    A = [1, -1]
    B = [-1, 1]
    C = [2, -1]
    D = [1, 1]
    E = [0, 2]
    M = [1, lambda_value]  # M depends on lambda

    # Combine all points into a single array
    points = np.array([A, B, C, D, E, M])

    # Perform Delaunay triangulation
    delaunay = Delaunay(points)

    # Get the triangles and edges
    triangles = delaunay.simplices  # Indices of points forming triangles
    edges = set()
    for tri in triangles:
        for i in range(3):
            edge = tuple(sorted([tri[i], tri[(i + 1) % 3]]))  # Edge as sorted tuple
            edges.add(edge)

    # Visualization
    plt.figure(figsize=(8, 6))
    plt.triplot(points[:, 0], points[:, 1], delaunay.simplices, color='blue', label="Triangulation")
    plt.scatter(points[:, 0], points[:, 1], color='red', s=100, label="Points")

    # Annotate points with labels
    labels = ['A', 'B', 'C', 'D', 'E', 'M']
    for i, (x, y) in enumerate(points):
        plt.text(x + 0.1, y, f"{labels[i]}", fontsize=12)

    plt.title(f"Delaunay Triangulation (λ = {lambda_value})")
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Compute the number of triangles and edges
    num_triangles = len(triangles)
    num_edges = len(edges)

    return num_triangles, num_edges, triangles, edges


# Example usage
lambda_value = 1  # Set lambda value
num_triangles, num_edges, triangles, edges = compute_triangulation_and_visualize(lambda_value)

# Print results
print(f"Lambda: {lambda_value}")
print(f"Number of triangles: {num_triangles}")
print(f"Number of edges: {num_edges}")
print("Triangles (by point indices):")
print(triangles)
print("Edges (by point indices):")
formatted_edges = {(int(a), int(b)) for a, b in edges}
print(formatted_edges)


