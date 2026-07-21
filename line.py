import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# User Input
n = int(input("Enter number of vertices: "))
print("Enter vertex names:")
vertices = input().split()

m = int(input("Enter number of edges: "))

print("\nEnter edges (Vertex1 Vertex2):")
for i in range(m):
    u, v = input(f"Edge {i+1}: ").split()
    G.add_edge(u, v)

# Create Line Graph
L = nx.line_graph(G)

# Draw Original Graph
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
pos1 = nx.spring_layout(G, seed=42)
nx.draw(G, pos1,
        with_labels=True,
        node_color="lightblue",
        node_size=700)
plt.title("Original Graph")

# Draw Line Graph
plt.subplot(1,2,2)
pos2 = nx.spring_layout(L, seed=42)
nx.draw(L, pos2,
        with_labels=True,
        node_color="lightgreen",
        node_size=700)
plt.title("Line Graph")

plt.show()

# Print vertices and edges of Line Graph
print("\nVertices of Line Graph:")
print(list(L.nodes()))

print("\nEdges of Line Graph:")
print(list(L.edges()))
