def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    st = [root]
    res = []
    
    while st:
        n = st.pop()
        if n:
            res.append(n.val)
            st.append(n.right)
            st.append(n.left)
    return res
