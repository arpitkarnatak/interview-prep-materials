
def reverseGraph(graph):
    reversedGraph = {_: [] for _ in graph}
    
    for node in graph:
        for neighbor in graph[node]:
            reversedGraph[neighbor].append(node)
    return reversedGraph

def dfs(graph, node, visited, ans):
    #print(f"On node {node} visited {visited}")
    if node in visited:
        #print(f"{node} already visited")
        return
    
    visited.add(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited, ans)
    ans += [node]
        
    
def strongly_connected_components(graph):
    visited, ans = set(), []
    #print(graph)
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, ans)
    print(ans)
    newGraph = reverseGraph(graph)
    print(newGraph)
    #print(ans)
    
    newVisited, count = set(),  0
    for node in ans:
        if node not in newVisited:
            print("SCC from node", node)
            dfs(graph, node, newVisited, [])
            count += 1
    #print(count)
    return count
    

# Example Usage:
graphs = [
    {
        "A": ["B"],
        "B": ["C"],
        "C": ["A", "D"],
        "D": ["E"],
        "E": ["F", "H"],
        "F": ["G"],
        "G": ["E", "H"],
        "H": [],
    },
    # Acyclic graph
    {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['E'],
        'E': []
    },
    # Graph with one strongly connected component
    {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['A'],
        'E': []
    },
    # Graph with multiple strongly connected components
    {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],
        'D': ['E'],
        'E': ['F'],
        'F': ['D']
    },
    # Single-node graph
    {
        'A': []
    },
    # Graph with a self-loop
    {
        'A': ['A'],
        'B': ['B'],
        'C': ['C']
    }
]

for graph in graphs:
    result = strongly_connected_components(graph)
    print("Graph ")
    print(f"Graph :{result} strongly connected component(s)")
    print("+================+")