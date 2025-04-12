import sys
sys.stdin = open('./disjoint-set/input.txt', 'r')
sys.stdout = open('./disjoint-set/output.txt', 'w')

class DisjointSet:
    def __init__(self):
        self.nodes = dict()

    def add(self, node):
        if node not in self.nodes:
            self.nodes[node] = None

    def findLeader(self, node):
        while self.nodes[node]:
            node = self.nodes[node]
        return node

    def union(self, source, target):
        leader = self.nodes[source]
        if leader is None:
            self.nodes[source] = target
        print(self.nodes)
        for node in self.nodes:
            ans, temp = [], node
            while self.nodes[temp]:
                ans.append(str(temp))
                temp = self.nodes[temp]
            ans.append(str(temp))
            print("->".join(ans))



disjoint = DisjointSet()
disjoint.add(1)
disjoint.add(4)
disjoint.add(6)
disjoint.add(7)
disjoint.union(7, 6)
disjoint.union(7, 4)

disjoint.print()
