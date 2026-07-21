import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

# Create Graph
G = nx.Graph()

# Input
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for i in range(m):
    u, v = input().split()
    G.add_edge(u, v)

# Draw Graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos,
        with_labels=True,
        node_color="skyblue",
        node_size=800,
        font_size=12)
plt.title("Given Graph")
plt.show()

# List of vertices
vertices = list(G.nodes())

found = False

# Check every permutation
for p in permutations(vertices):

    valid = True

    # Check consecutive edges
    for i in range(len(p) - 1):
        if not G.has_edge(p[i], p[i + 1]):
            valid = False
            break

    # Check last vertex connects to first
    if valid and G.has_edge(p[-1], p[0]):
        print("\nHamiltonian Cycle Found:")
        print(" -> ".join(p) + " -> " + p[0])
        found = True
        break

if not found:
    print("\nGraph is NOT Hamiltonian.")
