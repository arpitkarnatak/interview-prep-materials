import sys
sys.stdin = open('./Graphs/input.txt', 'r')
sys.stdout = open('./Graphs/output.txt', 'w')

class Solution:
    def dfsCycleDetector(self, graph, node, visited, parent):
        print(f"Came from {parent} --> {node} elems visited so far {visited}")
        visited.add(node)  # Move this line here to update visited for the current node

        for neighbor in graph[node]:
            if neighbor in visited and parent != neighbor:  # Update this line to check for the correct neighbor
                print(f"{neighbor} is already visited via some other node, Going from {node} --> {neighbor}")
                return True
            elif neighbor != parent:  # Update this line to check for the correct neighbor
                cycleExistInNeighbor = self.dfsCycleDetector(graph, neighbor, visited, node)
                if cycleExistInNeighbor:
                    return True
        return False

    def hasCycleUndirectedGraph(self, graph):
        visited, parent = set(), None

        for node in graph:
            if node not in visited:
                print(f"Checking for cycle from {node}")
                cycleExistInNeighbor = self.dfsCycleDetector(graph, node, visited, parent)
                if cycleExistInNeighbor:
                    return True
        return False


    def dfsHelperDirected(self, graph, node, visited, pathSoFar):
        print(f"On node {node} Path so far {pathSoFar}")
        if node in pathSoFar:
            print(f"{node} found in path so far {pathSoFar}")
            return True

        if node in visited:
            print(f"{node} is visited in some other path")
            return False
        
        visited.add(node)
        pathSoFar.add(node)
        for neighbor in graph[node]:
            if self.dfsHelperDirected(graph, neighbor, visited, pathSoFar):
                return True
        pathSoFar.remove(node)
        print(f"Node {node} not in path")
        return False

    def hasCycleDirectedGraph(self, graph):
        visited, path = set(), set()
        for node in graph:
            if node not in visited:
                if self.dfsHelperDirected(graph, node, visited, path):
                    return True
        print(visited, path)
        return False
ans = Solution()

testcases = [
    {
        "G": [],
        'F': ["D"],
        "E": ["D", "C"],
        "C": ["A", "E"],
        "A": ["B", "C"],
        "B": ["A", "D"],
        "D": ["B", "E", "F"],
}, {
    0: [1],
    1: []
}
]
res = []

for test in testcases:
    print(ans.hasCycleDirectedGraph(test))