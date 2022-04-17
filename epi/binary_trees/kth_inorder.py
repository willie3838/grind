'''

     1
  2       3
4  5

1st inorder: 2
2nd inorder: 1
3rd inorder: 3

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, root, node, left=None, right=None):
        if not root:
            return
        if node == root:
            root.left = left
            root.right = right
            return
        self.insert(root.left, node, left, right)
        self.insert(root.right, node, left, right)


def inorder(root, k):
    count = [0]
    return helper(root, k, count)

def helper(root, k, count):
    if not root:
        return None
    left = helper(root.left, k, count)
    count[0] += 1
    if count[0] == k:
        return root.val
    right = helper(root.right, k, count)

    return left or right



tree = [1,2,3,4,5]
'''
    1
  2   3
4  5

'''
def createTree(tree, i):
    root = None
    if i < len(tree):
        root = TreeNode(tree[i])
        root.left = createTree(tree, 2*i+1)
        root.right = createTree(tree, 2*i+2)
    return root
root = createTree(tree, 0)






print(inorder(root, 5))