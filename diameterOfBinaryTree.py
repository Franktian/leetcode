# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans =  0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth(root)
        return self.ans

    def depth(self, node):
        if node == None:
            return 0

        l = self.depth(node.left)
        r = self.depth(node.right)

        self.ans = max(self.ans, l + r)
        return max(l, r) + 1
