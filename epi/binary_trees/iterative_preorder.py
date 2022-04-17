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

    root -> left -> right
    postorder: left -> right -> root which is the opposite of root -> right -> left
    recursive call stack:

    [1,2,4]

    iterative call stack:
    [3,5,4]


        1
      2   3


    preorder: 1,2,3
    '''
    def preorder(root):
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
