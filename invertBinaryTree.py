class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
def invertTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c

    b.left = d
    b.right = e

    invertTree(a)
    
    print b.left.val
    print b.right.val
    