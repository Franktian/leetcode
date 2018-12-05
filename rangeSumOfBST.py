# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root == None:
            return 0
        
        queue = [root]
        res = 0
        
        while queue:
            node = queue.pop()
    
            if node:
                if node.val >= L and node.val <= R:
                    res += node.val
                
                if L < node.val:
                    queue.append(node.left)
                
                if R > node.val:
                    queue.append(node.right)
        return res