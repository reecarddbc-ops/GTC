import networkx as nx
import matplotlib.pyplot as plt

# Function to draw graph
def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(6,6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=800,
        font_size=12,
        font_weight="bold"
    )
    plt.title(title)
    plt.show()

# Create Graph
G = nx.Graph()

# Input vertices and edges
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

print("Enter edges (u v):")

for i in range(m):
    u, v = map(int, input().split())
    G.add_edge(u, v)

# Draw Graph
draw_graph(G, "Given Graph")

# Source and Destination
start = int(input("Enter starting vertex: "))
end = int(input("Enter ending vertex: "))

# Find all simple paths
paths = list(nx.all_simple_paths(G, source=start, target=end))

# In a simple graph, these paths are also trails
trails = paths

# Find closed walks (cycles)
closed_walks = nx.cycle_basis(G)

# Display Simple Paths
print("\nAll Simple Paths:")
for p in paths:
    print(" -> ".join(map(str, p)))

# Display Trails
print("\nAll Trails:")
for t in trails:
    print(" -> ".join(map(str, t)))

# Display Closed Walks
print("\nClosed Walks (Cycles):")
if len(closed_walks) == 0:
    print("No Closed Walks")
else:
    for c in closed_walks:
        c = c + [c[0]]
        print(" -> ".join(map(str, c)))
