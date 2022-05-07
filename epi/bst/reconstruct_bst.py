'''
            5
        3      10
    1     4   6   11

[1,3,4,5,6,10,11]


    5
3      10
[3,5,10]

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reconstruct(inorder):
    if inorder:
        mid = len(inorder)//2
        root = TreeNode(inorder[mid])
        root.left = reconstruct(inorder[:mid])
        root.right = reconstruct(inorder[mid+1:])

        return root
