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
        m = self.getHeight(root)
        n = 2 ** m - 1

        res = [["" for x in range(n)] for y in range(m)]

        queue = [root]
        l = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    left_padding = 2 ** (m - l - 1) - 1
                    spacing = 2 ** (m - 1) - 1
                    index = left_padding + (spacing + 1) * i
                    res[l][index] = str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            l += 1

        return res

    def getHeight(self, root):
        if not root:
            return 0
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        
        return max(l, r) + 1