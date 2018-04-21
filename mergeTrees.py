class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    
    # t1 is None, t2 is None
    if not t1 and not t2:
        return None

    if t1 and not t2:
        return t1
    
    if not t1 and t2:
        return t2

    t0 = TreeNode(t1.val + t2.val)

    t0.left = mergeTrees(t1.left, t2.left)
    t0.right = mergeTrees(t1.right, t2.right)
    
    return t0

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    
    d = TreeNode(4)
    e = TreeNode(5)
    #f = TreeNode(6)
    
    a.left = b
    a.right = c
    
    d.left = e
    #d.right = f
    
    n = mergeTrees(a, d)
    
    print n.val
    print n.left.val
    print n.right.val