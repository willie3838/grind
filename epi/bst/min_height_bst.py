'''

[1,2,3]

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct(arr):
    if arr:
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = construct(arr[:mid])
        root.right = construct(arr[mid+1:])
        return root