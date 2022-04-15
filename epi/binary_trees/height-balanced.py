class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


'''
        1
    2       
  5   6

'''
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.helper(root)[0]
    
def helper(self, root):
    if not root:
        return (True, -1)

    left = self.helper(root.left)
    right = self.helper(root.right)
    
    if not left[0] or not right[0]:
        return (False, 0)

    return (abs(left[1] + 1 - right[1] - 1) <= 1, max(left[1]+1, right[1]+1))