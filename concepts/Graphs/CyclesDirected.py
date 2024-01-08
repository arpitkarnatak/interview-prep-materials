

def dfsHelper(graph, node, pathSoFar, visited):
    print(f"On node {node}, path so far {pathSoFar}")
    
    if node in pathSoFar:
        print(f"Node {node} found in path")
        return True
        
    if node in visited:
        print(f"{node} is visited but not in this path, so it's not cyclic")
        return False
        
    pathSoFar.add(node)
    visited.add(node)
    
    for neighbor in graph[node]:
        foundCycle = dfsHelper(graph, neighbor, pathSoFar, visited)
        if foundCycle:
            return True
    pathSoFar.remove(node)
    print(f"Not found cycle, removed {node} from path {pathSoFar}")
    return False
    
def checkForCycle(graph):
    visited, parent, pathSoFar = set(), None, set()
    
    for node in graph:
        if node not in visited:
            hasCycle = dfsHelper(graph, node, pathSoFar, visited)
            if hasCycle:
                return True
    return False

graphs = [
    {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['E'],
        'E': []
    },
    {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['A'],
        'E': []
    },
    {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    },
    {
        'A': ['A']
    },
    {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
]


for index in range(len(graphs)):
    print(f"Graph {index + 1}")
    print(checkForCycle(graphs[index]))
    print("====================")