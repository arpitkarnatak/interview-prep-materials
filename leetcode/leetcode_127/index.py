import sys
sys.stdin = open('./leetcode_127/input.txt', 'r')
sys.stdout = open('./leetcode_127/output.txt', 'w')

class Solution:
    def __isValidSeq(self, word1, word2):
        differentLetters, index, loopCount = 0, 0, len(word1)

        while index < loopCount:
            if word1[index] != word2[index]:
                differentLetters += 1
            index += 1
            if differentLetters > 1:
                return False
        return True
    def __performBfsIteratively(self, start, end, words):
        ansTable = {word: None for word in words}
        ansTable[start] = 0

        queue = [[start, 0]]
        visited  = set()

        while queue:
            print(queue)
            topElemQueue = queue[0]
            word, seqLength = topElemQueue
            visited.add(word)
            if word == end:
                return seqLength
            for nextWord in words:
                if word != nextWord and nextWord not in visited:
                    if self.__isValidSeq(word, nextWord):
                        queue.append([nextWord, seqLength + 1])
            queue = queue[1:]
        return 0


    def ladderLength(self, beginWord, endWord, wordList):
        ans = self.__performBfsIteratively(beginWord, endWord, wordList)
        return ans


sol = Solution()
test1 = sol.ladderLength(
    "hit",
    "cog",
    ["hot","dot","dog","lot","log","cog"]
)
test2 = sol.ladderLength(
    "hit",
    "cog",["hot","dot","dog","lot","log"]
)
print(test1, test2)