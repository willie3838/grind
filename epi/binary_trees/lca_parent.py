class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TC: O(n)
# SC: O(n)

def findLCA(root, p, q):
    parents = {}
    helper(root, None, parents)

    ancestors = set()
    while p is not None:
        p = parents[p]
        ancestors.add(p)
    
    while q not in ancestors:
        q = parents[q]
    
    return q


def helper(root, parent, parents):
    if not root:
        return
    
    parents[root] = parent
    helper(root.left, root, parents)
    helper(root.right, root, parents)
    

