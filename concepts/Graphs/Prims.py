from heapq import heappop, heappush,heapify

class Solution:

    def distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    
    def __createWeightedGraph(self, points):
        allEdges = {_: [] for _ in range(len(points))}

        for point1Index in range(len(points) - 1):
            for point2Index in range(point1Index + 1, len(points)):
                point1, point2 = points[point1Index], points[point2Index]
                distance = self.distance(point1, point2)
                allEdges[point1Index].append([point2Index, distance])
                allEdges[point2Index].append([point1Index, distance])
        return allEdges


    def __primsAlgorithm(self, graph):
        minHeap = []
        visitedNodes = set([0])
        finalAns = 0

        for node in graph[0]:
            point2, weight = node
            heappush(minHeap, (weight, 0, point2))
        
        while minHeap:
            weight, point1, point2 = heappop(minHeap)
            if point2 not in visitedNodes:
                finalAns += weight
                visitedNodes.add(point2)

                for node in graph[point2]:
                    point, weight = node
                    if point not in visitedNodes:
                        heappush(minHeap, (weight, point2, point))
        return finalAns
            


    def minCostConnectPoints(self, points) -> int:

        if len(points) == 1:
            return 0

        graph = self.__createWeightedGraph(points)
        #print(edgesList)
        return self.__primsAlgorithm(graph)

        
        