import sys
sys.stdin = open('./leetcode_721/input.txt', 'r')
sys.stdout = open('./leetcode_721/output.txt', 'w')

accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]

'''

email1 <- email2
|
email3

'''

class DisjointSet:
    def __init__(self):
        self.graph = dict()

    def findLeader(self, item):
        while item in self.graph and self.graph[item]:
            item = self.graph[item]
        return item


    def add(self, fromNode, toNode=None):
        leaderFrom = self.findLeader(fromNode)
        leaderTo = self.findLeader(toNode) if toNode is not None else None

        if leaderFrom != leaderTo:
            self.graph[leaderFrom] = leaderTo

class Solution:

    def __emailToNameMap(self, accounts):
        emailNameMapping = dict()
        for accountItem in accounts:
            name, emails = accountItem[0], accountItem[1:]
            for email in emails:
                emailNameMapping[email] = name
        return emailNameMapping

    def __disjointSetGraph(self, accounts):
        graph = DisjointSet()
        for accountItem in accounts:
            emails = accountItem[1:]
            leaderEmail, childrenMail = emails[0], emails[1:]
            graph.add(leaderEmail)
            for email in childrenMail:
                graph.add(email, leaderEmail)
        return graph

    def __graphToArray(self, graph, emailNameMapping):
        del graph.graph[None]
        leaderEmails = dict()
        answer = []

        for email in graph.graph:
            leader = graph.findLeader(email)
            if leader in leaderEmails:
                leaderEmails[leader] += [email]
            else:
                leaderEmails[leader] = [email]
        for mail in leaderEmails:
            name = emailNameMapping[mail]
            #print(f"{mail}, {name} => {leaderEmails[mail]}")
            answer.append([name] + sorted(leaderEmails[mail]))
        return answer



    def accountsMerge(self, accounts):
        emailNameMapping = self.__emailToNameMap(accounts)
        graph = self.__disjointSetGraph(accounts)
        answer = self.__graphToArray(graph, emailNameMapping)
        return answer

solution = Solution()
print(solution.accountsMerge(accounts))