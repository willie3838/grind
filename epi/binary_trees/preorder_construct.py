class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    1
2       3

preorder: [1,2,null,null,3,null,null]

          1
    2           3
4       5   


preorder: [1,2,4,null,null,5,null,null,3,null,null]

TC: O(n)
SC: O(n)
'''
def reconstruct(preorder):
    root = preorder.pop(0)
    if not root:
        return root
    root.left = reconstruct(preorder)
    root.right = reconstruct(preorder)
    return root
