class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
        1
    2       3
 5    6

'''
def inorder(root):
    stack = []
    res = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            res.append(node.val)
            root = node.right
     
        
    return res
            

        
