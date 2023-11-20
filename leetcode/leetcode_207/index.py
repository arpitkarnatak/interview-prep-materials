import sys
sys.stdin = open('./leetcode_207/input.txt', 'r')
sys.stdout = open('./leetcode_207/output.txt', 'w')

'''
stack, visitedSet, ans
start with a random value on set

'''
def dfsHelper():
    pass
def canFinish(numCourses, prerequisites):

    if len(prerequisites) == 0:
        return True

    graph = {i: [] for i in range(numCourses)}
    for item in prerequisites:
        if item[0] == item[1]:
            return False
        graph[item[1]].append(item[0])

    print(graph)

    firstNode = list(graph.keys())[0] # node to start traversal from

    visitedNodes, stack = set(), [firstNode]

    while stack and len(visitedNodes) < numCourses:
        if stack[-1] not in visitedNodes:
            visitedNodes.add(stack[-1])
            print(f"Currently on Node {stack[-1]}")
            noNodeAdded = True
            for prerequisiteCourse in graph[stack[-1]]:
                if prerequisiteCourse in visitedNodes:
                    print("Cycle")
                    return False
                noNodeAdded = False
                stack.append(prerequisiteCourse)

            if noNodeAdded:
                print(f"No new node added for Node {stack[-1]}")
                visitedNodes.add(stack[-1])
                stack = stack[:-1]

            print(f"Stack => {stack}\nVisited => {visitedNodes}")
        else:
            return False

    return True

courses = 3
prerequisites = [[1,0]]

print(canFinish(courses, prerequisites))