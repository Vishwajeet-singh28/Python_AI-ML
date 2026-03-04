import networkx as nx

graph = nx.Graph()
while True:
    choice = int(input("Add an edge? (1 = yes, 2 = no): "))
    if choice == 1:
        u = input("Enter first node: ").strip().upper()
        v = input("Enter second node: ").strip().upper()
        wt = int(input("Enter edge weight: "))
        graph.add_edge(u, v, weight=wt)
    else:
        break
print("\nAdjacency List:")
for node, neighbors in graph.adj.items():
    print(node, neighbors)
start_node = input("Enter start node: ").strip().upper()
end_node = input("Enter goal node: ").strip().upper()
# Heuristic dictionary
heuristic = {end_node: 0}
for node in graph.nodes():
    if node != end_node:
        heuristic[node] = int(input(f"Heuristic value for {node}: "))
def h_func(curr, target):
    return heuristic[curr]
path = nx.astar_path(graph, start_node, end_node, heuristic=h_func, weight='weight')
path_cost = nx.astar_path_length(graph, start_node, end_node, heuristic=h_func, weight='weight')
print("Optimal Path: ", " -> ".join(path))
print("Total Cost: ", path_cost)
