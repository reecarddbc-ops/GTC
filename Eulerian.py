import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# User Input
n = int(input("Enter number of vertices: "))

print("Enter vertex names:")
vertices = input().split()

G.add_nodes_from(vertices)

m = int(input("Enter number of edges: "))

print("Enter edges (Vertex1 Vertex2):")

for i in range(m):
    u, v = input(f"Edge {i+1}: ").split()
    G.add_edge(u, v)

# Draw Graph
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos,
        with_labels=True,
        node_color="lightblue",
        node_size=700)

plt.title("Given Graph")
plt.show()

# Check Eulerian Circuit
if nx.is_eulerian(G):
    print("\nThe graph has an Eulerian Circuit.")

    print("\nEulerian Circuit:")

    circuit = list(nx.eulerian_circuit(G))

    for edge in circuit:
        print(edge)

else:
    print("\nThe graph does NOT have an Eulerian Circuit.")
