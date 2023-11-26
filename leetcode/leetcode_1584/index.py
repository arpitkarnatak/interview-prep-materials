import sys
sys.stdin = open('./leetcode_1584/input.txt', 'r')
sys.stdout = open('./leetcode_1584/output.txt', 'w')

class Solution:

    def distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    
    def minCostConnectPoints(self, points) -> int:

        allEdges = []

        for point1Index in range(len(points) - 1):
            for point2Index in range(point1Index + 1, len(points)):
                allEdges.append([self.distance(points[point1Index], points[point2Index]), point1Index, point2Index])

        print(allEdges)
        allEdges = sorted(allEdges)

        visited, totalCost = set(), 0

        while len(visited) < len(points):
            if allEdges[0][1] not in visited or allEdges[0][2] not in visited:
                totalCost += allEdges[0][0]
                visited.add(allEdges[0][1])
                visited.add(allEdges[0][2])

            allEdges = allEdges[1:]
        return totalCost


ans = Solution()

testcases = [
    [[0,0],[2,2],[3,10],[5,2],[7,0]],
    [[3,12],[-2,5],[-4,1]],
    [[2,-3],[-17,-8],[13,8],[-17,-15]]
]

for test in testcases:
    print(ans.minCostConnectPoints(test))
