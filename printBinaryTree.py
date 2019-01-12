# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.getHeight(root)
        width = 2 ** height - 1
        res = [["" for i in range(width)] for i in range(height)]

        queue = [root]
        l = 0

        while queue and l < height:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    left_padding = 2 ** (height - l - 1) - 1
                    spacing = 2 ** (height - l) - 1
                    index = left_padding + (spacing + 1) * i
                    res[l][index] = str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    # Key to make up empty space
                    queue.append(None)
                    queue.append(None)
            l += 1
        return res

    def getHeight(self, root):
        if root == None:
            return 0

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
