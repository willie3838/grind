class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    1
   2  4
  3

TC: O(n) where n is the number of nodes
SC: O(n) where n is the nubmer of nodes
'''


# def findExterior(root):
#     curr = []
#     curr.append(root)
#     left = []
#     right = []
#     leaves = []
#     res = [root.val]

#     while curr:
#         level = []
#         for node in curr:
#             if node.left:
#                 level.append(node.left)
#             if node.right:
#                 level.append(node.right)

#         if level:
#             left.append(level[0].val)
#             right.append(level[-1].val)
#             leaves = [node.val for node in level[1:-1]]
#         curr = level

#     return res + left + leaves + right[::-1]


def findExterior(root):
    left = leftView(root)
    right = rightView(root)
    leaves = findLeaves(root)[1:-1]

    return left + right[1:][::-1] + leaves[1:-1]

def leftView(root):
    if not root:
        return []
    left = leftView(root.left)
    right = leftView(root.right)
    
    if len(left) <= len(right):
        return [root.val] + left
    else:
        return [root.val] + left + right[len(left):]

def rightView(root):
    if not root:
        return []
    left = rightView(root.left)
    right = rightView(root.right)
    
    if len(right) >= len(left):
        return [root.val] + right
    else:
        
        return [root.val] + right + left[len(right):]


def findLeaves(root):
    if not root:
        return []
    if not root.left and not root.right:
        return [root.val]
    
    return findLeaves(root.left) + findLeaves(root.right)
    

'''
        1
    2       3
4       5


[1,2,4,5,3]
'''
tree = [1,2,3,4,5]
def createTree(tree, i):
    root = None
    if i < len(tree):
        root = TreeNode(tree[i])
        root.left = createTree(tree, 2*i+1)
        root.right = createTree(tree, 2*i+2)
    return root
root = createTree(tree, 0)

print(findExterior(root))