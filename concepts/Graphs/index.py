import sys
sys.stdin = open('./Graphs/input.txt', 'r')
sys.stdout = open('./Graphs/output.txt', 'w')


class Solution:
    def arrToMatrix(self, matrix):
        graph = {index: [] for index in range(len(matrix))}
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix)):
                if matrix[rowIndex][colIndex] == 1 and rowIndex != colIndex:
                    graph[rowIndex].append(colIndex)
        return graph

    def performDfs(self, graph):
        provinces, stack, visited = 0, [], set()

        for node in graph.keys():
            if node in visited:
                pass
            else:
                stack.append(node)
                visited.add(node)
                while stack != []:
                    somethingAdded = False
                    for neighbor in graph[stack[-1]]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
                            somethingAdded = True

                    if not somethingAdded:
                        stack.pop()
                provinces += 1
        return provinces

    def findCircleNums(self, isConnected):
        graph = self.arrToMatrix(isConnected)
        ans = self.performDfs(graph)
        return ans

ans = Solution()

ans1 = ans.findCircleNums([[1,1,0],[1,1,0],[0,0,1]])
ans2 = ans.findCircleNums([[1,0,0],[0,1,0],[0,0,1]])

print(f"Ans 1 => {ans1}\nAns 2 => {ans2}")

