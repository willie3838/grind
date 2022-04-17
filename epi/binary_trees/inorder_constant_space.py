class TreeNode:
    def __init__(self, val, parent, left=None, right=None):
        self.parent = parent
        self.val = val
        self.left = left
        self.right = right

'''

            1
        2       3
    4      5
Inorder: left -> root -> right

[1,2,4,5,3]
- use a double ended queue


[4,2,5,1,3]
'''

'''

This algo takes advantage of the following:
- inorder traversal goes down the left subtree then goes
to the node's right subtree or back to the parent
- if it comes up from the right subtree, it has to go back up to the parent
- need to have a previous variable to understand when the traversal went down the left vs the right

'''
def inorder(root):
    prev, res = None, []

    while root:
        # traverse down a subtree
        if prev is root.parent:
            # if we have a left subtree keep going
            if root.left:
                nextt = root.left
            # done with left, go right if it exists or parent
            else:
                res.append(root.val)
                nextt = root.right or root.parent
        # came up from left subtree, can either
        # go right or to the parent
        elif root.left is prev:
            res.append(root.val)
            nextt = root.right or root.parent
        # came up from right subtree, go up to the parent
        else:
            nextt = root.parent
        prev, root = root, nextt
    return res

# from collections import deque
# def inorder(root):
#     res = deque()

#     while True:
#         if root:
#             res.append(root)
#             root = root.right
#         elif type(res[-1]) == int:
#             return res
#         else:
#             node = res.pop()
#             res.appendleft(node.val)
#             root = node.left

# tree = [1,2,3,4,5]
# def createTree(tree, i):
#     root = None
#     if i < len(tree):
#         root = TreeNode(tree[i])
#         root.left = createTree(tree, 2*i+1)
#         root.right = createTree(tree, 2*i+2)
#     return root
# root = createTree(tree, 0)

# print(inorder(root))
    