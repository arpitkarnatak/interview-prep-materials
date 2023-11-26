import sys
sys.stdin = open('./Recursion/input.txt', 'r')
sys.stdout = open('./Recursion/output.txt', 'w')


class Concept:
    def allPermutations(self, word):
        ans = []

        def backtrack(processed, unprocessed):
            #print(f"Processed => {processed} Unprocessed => {unprocessed}")
            if unprocessed == "":
                #print("Ans", processed)
                ans.append(processed)
                return
            
            for index in range(len(processed) + 1):
                backtrack(processed[:index] + unprocessed[0] + processed[index:], unprocessed[1:])
            return
        backtrack("", word)
        return ans

    def allSubsequences(self, word):
        ans = []
        def backtrack(processed, unprocessed):
            if unprocessed == "":
                ans.append(processed)
                return

            backtrack(processed+unprocessed[0], unprocessed[1:])
            backtrack(processed, unprocessed[1:])

        backtrack("", word)
        return list(ans)

    def allSubstrings(self, word):
        ans = set()
        def backtrack(processed, unprocessed):
            ans.add(processed)
            if unprocessed == "":
                return
            backtrack(processed + unprocessed[0], unprocessed[1:])
            backtrack(unprocessed[0], unprocessed[1:])
        backtrack("", word)
        return list(ans)



ans = Concept()
testcases = [
    "abc",
    "pqrs",
    "helo"
]
for item in testcases:
    print("Permutations => ", ans.allPermutations(item))
    print("Subsequences => ", ans.allSubsequences(item))
    print("Substrings => ", ans.allSubstrings(item))
