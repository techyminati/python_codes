# Finds total connected components along with corresponding length in the graph
def connected_components(graph):
    visited = set()
    connected_components = []
    connected_components_length = []
    for vertex in list(graph.keys()):
        if vertex not in visited:
            components = set()
            leaves = []
            length = 0
            leaves.append(vertex)
            while leaves:
                leaf = leaves.pop()
                visited.add(leaf)
                components.add(leaf)
                for connected_vertex in graph[leaf]:
                    if connected_vertex not in visited:
                        length += 1
                        leaves.append(connected_vertex)
            connected_components.append(components)
            connected_components_length.append(length)
    return [connected_components, connected_components_length]

# Creates the undirected graph using adjacency list from the user input
graph_adj_list = {}

total_nodes = int(input("Enter total nodes: "))
for i in range(total_nodes):
    node = int(input("Enter node: "))
    graph_adj_list[node] = list(map(int,input("Enter neighbors: ").split()))

print("Graph is ",graph_adj_list)

connected_components, connected_components_length = map(list, connected_components(graph_adj_list))

# Total number of components
total_components = len(connected_components)
print("Total number of components in the graph:",total_components)

# Prints length of each component:
for index in range(len(connected_components)):
    print("Length of connected component having vertices", connected_components[index], "is", connected_components_length[index])

# Finds largest connected component
index_of_largest_component = connected_components_length.index(max(connected_components_length))
print("Largest connected component is with vertices", connected_components[index_of_largest_component])


'''
Input/Output:

Enter total nodes: 11
Enter node: 1
Enter neighbors: 2 3
Enter node: 2
Enter neighbors: 1 4
Enter node: 3
Enter neighbors: 1 4 5 6
Enter node: 4
Enter neighbors: 2 3 5
Enter node: 5
Enter neighbors: 3 4
Enter node: 6
Enter neighbors: 3
Enter node: 7
Enter neighbors: 8 9
Enter node: 8
Enter neighbors: 7 9
Enter node: 9
Enter neighbors: 7 8
Enter node: 10
Enter neighbors: 11
Enter node: 11
Enter neighbors: 10
Graph is  {1: [2, 3], 2: [1, 4], 3: [1, 4, 5, 6], 4: [2, 3, 5], 5: [3, 4], 6: [3], 7: [8, 9], 8: [7, 9], 9: [7, 8], 10: [11], 11: [10]}
Total number of components in the graph: 3
Length of connected component having vertices {1, 2, 3, 4, 5, 6} is 7
Length of connected component having vertices {8, 9, 7} is 3
Length of connected component having vertices {10, 11} is 1
Largest connected component is with vertices {1, 2, 3, 4, 5, 6}
'''
