class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root):
    if not root:
        return True

    l = checkDepth(root.left)
    r = checkDepth(root.right)
    
    return abs(l - r) <= 1 and isBalanced(root.left) and isBalanced(root.right)

def checkDepth(root):
    if not root:
        return 0

    l = checkDepth(root.left)
    r = checkDepth(root.right)

    return max(l, r) + 1

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    #f = TreeNode(6)

    a.left = b
    a.right = c
    
    c.left = d
    #d.right = f
    
    n = checkDepth(a)
    print n
