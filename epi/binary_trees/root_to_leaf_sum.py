class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
  1
2   3  

sum = 6

'''

def sumNumbers(root):
    return helper(root, 0)
        
def helper(root, path):
    if not root:
        return 0
    if not root.left and not root.right:
        return path*10 + root.val

    return helper(root.left, path*10 + root.val)+helper(root.right, path*10 + root.val)
