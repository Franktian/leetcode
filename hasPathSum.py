def hasPathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    
    if root.left == None and root.right == None and root.val == sum:
        return True
    
    sum -= root.val
    
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
