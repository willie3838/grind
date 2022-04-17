class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
'''
        1
    2      3
4      5


brute force:
- do inorder and store it in an array
- traverse array and return the curr index + 1
- TC: O(n) SC: O(n)

optimized
- use helper function and do inorder traversal with a parameter that has the previous node
- when the previous node is the target, return the current node
- TC: O(n) SC: O(h)

'''
def findInorderSuccessor(root, target):
    prev = [None]
    return helper(root, target, prev)

def helper(root, target, prev):
    if not root:
        return None
    left = helper(root.left, target, prev)
    if prev[0] and prev[0].val == target:
        return root.val
    prev[0] = root
    right = helper(root.right, target, prev)

    return left or right
    

tree = [1,2,3,4,5]
def createTree(tree, i):
    root = None
    if i < len(tree):
        root = TreeNode(tree[i])
        root.left = createTree(tree, 2*i+1)
        root.right = createTree(tree, 2*i+2)
    return root
root = createTree(tree, 0)

print(findInorderSuccessor(root, 4))