# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = collections.defaultdict(list)
        
        queue = [(root, 0)]
        
        while queue:
            node, index = queue.pop(0)
            
            if node:
                res[index].append(node.val)
                
                if node.left:
                    queue.append((node.left, index - 1))
                
                if node.right:
                    queue.append((node.right, index + 1))
        
        sort_keys = res.keys()
        
        sort_keys.sort()
        
        lst = []
        
        for k in sort_keys:
            lst.append(res[k])
        
        return lst