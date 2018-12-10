# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path):
            if root:
                path += str(root.val)
                
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += "->"
                    dfs(root.left, path)
                    dfs(root.right, path)
        
        res = []
        dfs(root, "")
        return res

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        res = []
        
        st = [(root, str(root.val))]
        
        while st:
            node, path = st.pop()
            if not node.left and not node.right:
                res.append(path)
            
            if node.left:
                st.append((node.left, path + '->' + str(node.left.val)))
            
            if node.right:
                st.append((node.right, path + '->' + str(node.right.val)))
        
        return res
