import sys
sys.stdin = open('./leetcode_743/input.txt', 'r')
sys.stdout = open('./leetcode_743/output.txt', 'w')

global MAX_LIMIT
MAX_LIMIT = 1000000000
class Solution:

    def dijkstra(self, graph, start):
        visited, timeToReachNode, stack = set([start]), [MAX_LIMIT for i in range(len(graph))], [(start, 0)]

        # Since nodes are 1 to N, NODE-1 should be index for modifying
        timeToReachNode[start - 1] = 0

        while stack != []:
            print(f"Stack => {stack}\nVisited => {visited}\nTime => {timeToReachNode}\n=================")
            addedToStack = False
            topNode = stack[-1]
            print("F", topNode[0])
            for neighbor in graph[topNode[0]]:
                if neighbor[0] not in visited:
                    addedToStack = True
                    tupleItem = tuple((neighbor[0], topNode[1] + neighbor[1]))
                    stack.append(tupleItem)
                    visited.add(neighbor[0])
                    timeToReachNode[neighbor[0] - 1] = min(timeToReachNode[neighbor[0] - 1], topNode[1] + neighbor[1])
                else:
                    tupleItem = tuple((neighbor[0], topNode[1] + neighbor[1]))
                    if timeToReachNode[neighbor[0] - 1] > topNode[1] + neighbor[1]:
                        print(f"{neighbor[0]} already reached, \n({neighbor[0]}, {timeToReachNode[neighbor[0] - 1]}) should be popped")
                        stack.append((neighbor[0], topNode[1] + neighbor[1] ))
                        timeToReachNode[neighbor[0] - 1] = topNode[1] + neighbor[1]
                                
            if not addedToStack:
                print(f"Popping top {stack[-1]}")
                stack.pop()
        return timeToReachNode
    def graphFromArray(self, arr, n):
        graph = {i: [] for i in range(1, n+1)}
        for path in arr:
            graph[path[0]].append([path[1], path[2]])
        return graph

    def networkDelayTime(self, times, n, k) -> int:
        graph = self.graphFromArray(times, n)
        print(graph)
        res = self.dijkstra(graph, k)
        if MAX_LIMIT in res:
            return -1
        return sum(res)


testcases = [
    # {
    #     "times": [[2,1,1],[2,3,1],[3,4,1]],
    #     "n": 4,
    #     "k": 2
    # },
    # {
    #     "times": [[1,2,1]],
    #     "n": 2,
    #     "k": 1
    # },
    # {
    #     "times": [[1,2,1]],
    #     "n": 2,
    #     "k": 2
    # },
    {
        "times":  [[1,2,1],[2,3,2],[1,3,4]],
        "n": 3,
        "k": 1
    }
   
]

ans = Solution()
for test in testcases:
    print(ans.networkDelayTime(test["times"], test["n"], test["k"]))
    print("=========END===========")