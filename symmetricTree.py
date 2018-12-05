# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        
        while queue:
            l = len(queue)
            lst = []
            for i in range(l):
                node = queue.pop(0)
                if node:
                    lst.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    lst.append(0)

            for i in range(len(lst) / 2):
                if lst[i] != lst[len(lst) - 1 - i]:
                    return False

        return True