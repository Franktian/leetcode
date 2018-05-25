def preorderTraversal(root):
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

def inorderTraversal(root):
        pass

def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]

    Modified version of preorder:
    - root -> right -> left
    - reverse the order of the results
    """
    st = [root]
    res = []
    
    while st:
        n = st.pop()
        if n:
            res.append(n.val)
            st.append(n.left)
            st.append(n.right)
    return res[::-1]
