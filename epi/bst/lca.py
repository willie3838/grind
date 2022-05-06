
'''

            5
        4       10
    3         6       


    - if one node is less than the root and the other is greater, the root is the ancestor
    - if the root is one of the nodes then return the root
    - keep traversing otherwise 
'''


def findLCA(root, p, q):
    if p < root.val and q > root.val or p > root.val and q < root.val:
        return root.val
    elif root == p or root == q:
        return root.val
    elif p > root.val:
        return findLCA(root.right, p, q)
    else:
        return findLCA(root.left, p, q)
