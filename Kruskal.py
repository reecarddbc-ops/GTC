import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# User Input
n = int(input("Enter number of vertices: "))

print("Enter vertex names:")
vertices = input().split()

m = int(input("Enter number of edges: "))

print("\nEnter edges in the format: Vertex1 Vertex2 Weight")

for i in range(m):
    u, v, w = input(f"Edge {i+1}: ").split()
    G.add_edge(u, v, weight=int(w))

# Find Minimum Spanning Tree using Kruskal
mst = nx.minimum_spanning_tree(G, algorithm="kruskal")

# Draw Graphs
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12,5))

# Original Graph
plt.subplot(1,2,1)
nx.draw(G, pos, with_labels=True,
        node_color="lightblue",
        node_size=700)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Original Graph")

# MST
plt.subplot(1,2,2)
nx.draw(mst, pos, with_labels=True,
        node_color="lightgreen",
        node_size=700)
mst_labels = nx.get_edge_attributes(mst, "weight")
nx.draw_networkx_edge_labels(mst, pos, edge_labels=mst_labels)
plt.title("Minimum Spanning Tree")

plt.show()

# Print MST
print("\nEdges in Minimum Spanning Tree:")
total = 0

for u, v, w in mst.edges(data=True):
    print(u, "--", v, " Weight =", w["weight"])
    total += w["weight"]

print("Total Weight =", total)
