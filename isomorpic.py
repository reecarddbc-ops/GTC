import networkx as nx
import matplotlib.pyplot as plt

# -------- Graph 1 --------
G1 = nx.Graph()

v1 = input("Enter vertices of Graph 1: ").split()
G1.add_nodes_from(v1)

e1 = int(input("Enter number of edges in Graph 1: "))

print("Enter edges of Graph 1:")
for i in range(e1):
    u, v = input().split()
    G1.add_edge(u, v)

# -------- Graph 2 --------
G2 = nx.Graph()

v2 = input("\nEnter vertices of Graph 2: ").split()
G2.add_nodes_from(v2)

e2 = int(input("Enter number of edges in Graph 2: "))

print("Enter edges of Graph 2:")
for i in range(e2):
    u, v = input().split()
    G2.add_edge(u, v)

# -------- Check Isomorphism --------
if nx.is_isomorphic(G1, G2):
    print("\nGraphs are Isomorphic")
else:
    print("\nGraphs are Not Isomorphic")

# -------- Display Graphs --------
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
nx.draw(G1, with_labels=True, node_color="lightblue", node_size=700)
plt.title("Graph 1")

plt.subplot(1,2,2)
nx.draw(G2, with_labels=True, node_color="lightgreen", node_size=700)
plt.title("Graph 2")

plt.show()
