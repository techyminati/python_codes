# Program to find whether cycle exists in a graph

def search(graph, vertex, visited, parent):
    visited[vertex] = True
    
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if search(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True
        
    return False
            
def has_cycle(graph):
    visited = {v: False for v in graph.keys()}
    
    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, None):
                return True
            
    return False


# Creates the undirected graph using adjacency list from the user input
graph_adj_list = {}

total_nodes = int(input("Enter total nodes: "))
for i in range(total_nodes):
    node = int(input("Enter node: "))
    graph_adj_list[node] = list(map(int,input("Enter neighbors: ").split()))

print("Graph is ",graph_adj_list)

hascycle = has_cycle(graph_adj_list)
print("Graph has cycle") if hascycle else print("Graph has no cycle")

''' 
Input/ Output:

Enter total nodes: 6
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
Graph is  {1: [2, 3], 2: [1, 4], 3: [1, 4, 5, 6], 4: [2, 3, 5], 5: [3, 4], 6: [3]}
Graph has cycle

'''