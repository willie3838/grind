from libcst import RightShift


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

    '''
    
        1
      2   3
    4  5

      preorder: 1,2,4,5,3


        1
      2   3


    preorder: 1,2,3
    '''
    def preorder(root):
        stack = []
        res = []

        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res
