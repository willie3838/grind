class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


'''

     1
  2     3
       4

'''
def maxDepth(root):
    if not root:
        return 0
    left = 1 + maxDepth(root.left)
    right = 1 + maxDepth(root.right)
    return max(left, right)