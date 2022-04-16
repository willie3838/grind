class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''

    1
   2  3

   p=2,q=3,LCA=1


       1
   2       3
5    6 

p=2,q=5,LCA=2
'''

def findLCA(root, p, q):
    return helper(root, None, p, q)[1]

'''

this function takes advantage of the following cases:
- if the two nodes are in the same subtree, the LCA the node with the highest height  (assuming we're traversing from bottom-up)
- if the two nodes are in different subtrees, the LCA is the current node (assuming we're traversing from bottom-up)

TC: O(n) where n is the number of nodes 
SC: O(h) where h is the height of the tree


notes:
- LCA can be broken down into the case: if the two nodes are in different subtrees, the root is the LCA. or if the
current node is one of the nodes then that becomes the LCA.
otherwise, need to traverse in the subtree where they're both present and check if they're in different subtrees
or the current node is a target
'''
def helper(root, p, q):
    if not root:
        (0, None)
    
    left = helper(root.left, root, p, q)
    if left[0] == 2:
        return left
    
    right = helper(root.right, root, p, q)
    if right[0] == 2:
        return right

    
    found = right[0] + left[0]
    if root == p or root == q:
        found += 1
    
    return (found, root if found == 2 else None)

    




    

