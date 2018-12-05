# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [(root, root.val)]
        res = 0
        
        while queue:
            node, v = queue.pop(0)
            
            if node:
                if not node.left and not node.right:
                    res += v
                
                if node.left:
                    queue.append((node.left, v * 10 + node.left.val))
                
                if node.right:
                    queue.append((node.right, v * 10 + node.right.val))
        return res