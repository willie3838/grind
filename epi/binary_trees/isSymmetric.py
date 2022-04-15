class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


# TC: O(n) where n is the number of nodes
# SC: O(h) where h is the height of the tree
def isSymmetric(root):
    if not root:
        return True
    return helper(root.left, root.right)

def helper(left, right):
    # the case when the root node is a leaf
    if not left and not right:
        return True
    
    # case when it's asymmetric: one node is null or the values don't match
    if not left and right or not right and left:
        return False
    if left.val != right.val:
        return False
    
    
    return helper(left.left, right.right) and helper(left.right, right.left)