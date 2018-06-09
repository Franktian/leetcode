def longestUnivaluePath(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.res = 0
    def traverse(node):
        if not node:
            return 0
        left_len = traverse(node.left)
        right_len = traverse(node.right)

        left = 0
        right = 0
        if node.left and node.left.val == node.val:
            left = left_len + 1
        if node.right and node.right.val == node.val:
            right = right_len + 1
        self.res = max(self.res, left + right)
        return max(left, right)
    traverse(root)
    return self.res