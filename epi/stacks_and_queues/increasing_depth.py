class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

'''
        1
    2        3
  4   5    6   7

'''
import collections
def levelOrder(root):
    curr = [root]
    res = []

    # TC: O(n) because we'll go through every single node in the tree in all cases
    # SC: O(n)
    while curr:
        res.append([node.val for node in curr])

        level = []
        for node in curr:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        curr = level
    
    return res

        