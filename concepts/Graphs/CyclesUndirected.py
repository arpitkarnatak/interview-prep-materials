

def dfsHelper(graph, node, parent, visited):
    print(f"{parent} ---> {node}")
    
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited:
            if parent != neighbor:
                print(f"{neighbor} is already visited but not by {parent}")
                return True
            else:
                pass
        else:
            hasCycle = dfsHelper(graph, neighbor, node, visited)
            if hasCycle:
                return True
    print(f"No cycle found after {node}, go back")
    return False

def checkForCycle(graph):
    visited, parent = set(), None
    
    for node in graph:
        if node not in visited:
            hasCycle = dfsHelper(graph, node, parent, visited)
            if hasCycle:
                return True
    return False

# Test Case 1: Acyclic graph
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

# Test Case 2: Cyclic graph
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

# Test Case 3: Disconnected graph
graph3 = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E'],
    'E': ['D']
}

# Test Case 4: Single-node graph
graph4 = {
    'A': []
}

# Test Case 5: Graph with self-loop
graph5 = {
    'A': ['A'],
    'B': ['B'],
    'C': ['C']
}

graphs = [graph1, graph2, graph3, graph4, graph5]

for index in range(len(graphs)):
    print(f"Graph {index + 1}")
    print(checkForCycle(graphs[index]))
    print("====================")