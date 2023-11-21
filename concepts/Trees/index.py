import sys
sys.stdin = open('./Trees/input.txt', 'r')
sys.stdout = open('./Trees/output.txt', 'w')

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


    def addNode(self, val):
        currentPos = self

        while currentPos is not None:
            if currentPos.val > val:
                currentPos = currentPos.left
            else:
                currentPos = currentPos.right
        
        currentPos = TreeNode(val)


class Solution:
    def addNode(self, root, val):
        # If empty tree (or subtree), this line would return a node
        if root is None:
            return TreeNode(val)

        # Move to left subtree if val > current subtree root
        if root.val > val:
            root.left = self.addNode(root.left, val)
        # Move to right subtree if val > current subtree root
        else:
            root.right = self.addNode(root.right, val)

        # Finally return the main node
        return root


    def preOrder(self, root):
        if root is None:
            return []
        return [root.val] + self.preOrder(root.left) +  self.preOrder(root.right)  

    def inOrder(self, root):
        if root is None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return []
        return self.postOrder(root.left) +  self.postOrder(root.right) + [root.val] 


    def levelOrder(self, root):
        if not root:
            return []

        queue, ans = [[root]], []

        while queue != []:
            currentLevelNodes = queue[0]
            nextLevelNodes = []
            for node in currentLevelNodes:
                if node.left:
                    nextLevelNodes.append(node.left)
                if node.right:
                    nextLevelNodes.append(node.right)

            if nextLevelNodes != []:
                queue.append(nextLevelNodes)
            ansLevel = list(filter(lambda x: x != [],[[] if not node else node.val for node in currentLevelNodes]))
            ans.append(ansLevel)
            queue = queue[1:]
        return ans

    def zigZagTraversal(self, root):
        array = self.levelOrder(root)
        return [array[i] if i%2 == 0 else array[i][::-1] for i in range(len(array))]


    def heightOfTree(self, root):
        if root is None:
            return 0

        return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))

    def diameterOfTree(self, root):
        if root is None:
            return 0
        return max(1 + self.heightOfTree(root.left) + self.heightOfTree(root.right), self.diameterOfTree(root.left), self.diameterOfTree(root.right))



ans = Solution()

inputFile = list(map(int, input().split(" ")))


root = TreeNode(inputFile[0])

for nodeValue in inputFile[1:]:
    ans.addNode(root, nodeValue)


preOrderTraversal = ans.preOrder(root)
inOrderTraversal = ans.inOrder(root)
postOrderTraversal = ans.postOrder(root)
levelOrderTraversal = ans.levelOrder(root)
zigZagTraversal = ans.zigZagTraversal(root)
heightOfTree = ans.heightOfTree(root)


print(f"Pre => {preOrderTraversal}\nIn => {inOrderTraversal}\nPost => {postOrderTraversal}\nLevel => {levelOrderTraversal}\nZigZag => {zigZagTraversal}")
print(f"Height Of Tree => {heightOfTree}")

diameterOfTree = ans.diameterOfTree(root)
print(f"Diameter => {diameterOfTree}")