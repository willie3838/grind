class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSum(root, k):
    if not root:
        return False
    if not root.left and not root.right and k - root.val == 0:
        return True
    return findSum(root.left, k - root.val) or findSum(root.right, k - root.val)