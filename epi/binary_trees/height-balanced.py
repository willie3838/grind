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
def isHeightBalanced(root):
    return helper(root)


def helper(root):
    if not root:
        return 0

    left = helper(root.left)
    right = helper(root.right)

    if left == -1 or right == -1:
        return -1
    if abs(left-right) > 1:
        return -1

    return max(left, right) + 1