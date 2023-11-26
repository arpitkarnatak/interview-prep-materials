import sys
sys.stdin = open('./leetcode_547/input.txt', 'r')
sys.stdout = open('./leetcode_547/output.txt', 'w')


'''
Number of Provinces:
https://leetcode.com/problems/number-of-provinces/description/
'''
class Solution:
    # Convert the 2D Array into a Matrix
    def arrToMatrix(self, matrix):
        graph = {index: [] for index in range(len(matrix))}
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix)):
                if matrix[rowIndex][colIndex] == 1 and rowIndex != colIndex:
                    graph[rowIndex].append(colIndex)
        return graph

    # Perform DFS on the Graph
    def performDfs(self, graph):
        provinces, stack, visited = 0, [], set()

        # Traverse through each key
        for node in graph.keys():
            # Node is already visited
            if node in visited:
                pass
            else:
                # Stack filled with node
                stack.append(node)
                visited.add(node)
                while stack != []:
                    somethingAdded = False
                    # Only add neighbor if it's not visited
                    for neighbor in graph[stack[-1]]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)
                            somethingAdded = True
                    # Nothing is added, so push out the top element
                    if not somethingAdded:
                        stack.pop()
                provinces += 1
        return provinces

    def findCircleNum(self, isConnected):
        graph = self.arrToMatrix(isConnected)
        ans = self.performDfs(graph)
        return ans

ans = Solution()

ans1 = ans.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
ans2 = ans.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])

print(f"Ans 1 => {ans1}\nAns 2 => {ans2}")

