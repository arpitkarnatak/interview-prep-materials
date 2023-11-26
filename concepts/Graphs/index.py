import sys
sys.stdin = open('./Graphs/input.txt', 'r')
sys.stdout = open('./Graphs/output.txt', 'w')

class Solution:
    def hasCycleUndirectedGraph(self, graph):
        visited = set()


        # Perform recursive DFS to detect Cycles
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    if neighbor != parent:
                        return True
                else:
                    return dfs(neighbor, node)
            return False

        for node in graph:
            if node not in visited:
                if dfs(node, -1):
                    return True
        return False

    def hasCycleDirectedGraph(self, graph):
        visited, path = set(), set()
        def dfs(node):
            if node in path:
                return True
            if node in visited:
                return False

            path.add(node)
            visited.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            path.remove(node)
            return False

        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False
ans = Solution()

testcases = [
    {
    0: [1, 2],
    1: [],
    2: [],
    3: [2]
},{
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
},
{
    0: [1],
    1: [0]
},
{
    0: [],
    1: [4],
    2: [4],
    3: [1,2],
    4: []
}
]
res = []

for test in testcases:
    print(ans.hasCycleUndirectedGraph(test), ans.hasCycleDirectedGraph(test))