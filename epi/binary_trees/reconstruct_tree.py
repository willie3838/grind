class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''

    1
2       3

inorder: [2,1,3]
preorder: [1,2,3]


        1
  2           3
4   5

  inorder: [4,2,5,1,3]
  preorder: [1,2,4,5,3]


        1
  2           3
4   5       6   7

  inorder: [4,2,5,1,6,3,7]
  preorder: [1,2,4,5,3,6,7]


- find the root from preorder
- find the index of the root in inorder, set the left and right to the two elements in between


Recursive algorithm takes advantage of the fact that the root in an inorder traversal always splits its
left and right subtrees. Therefore, using the preorder to find the root allows us to create the
left and right subtrees

Iterative algorithm builds the tree using the preorder traversal and uses the inorder traversal
to justify whether a node goes in the right or left subtree. We put a node in the left subtree
if its index in the inorder is less than the previous traversed node. Otherwise, we
go upwards in the constructed tree until we find greatest node that is less than the current node's
position in the inoreder traversal and the current node will be in the right subtree of that


TC: O(n) where n is the number of nodes
SC: O(n) where n is the number of nodes
'''


'''
    1
2       3

Inorder: [2,1,3]
Preorder: [1,2,3]
'''
def buildTree(self, preorder, inorder):

    # # construct hashmap mapping a value to its inorder index
    # idx = {} 
    # for i, val in enumerate(inorder):
    #     idx[val] = i 
			
	# # Iterate over preorder and construct the tree 
    # stack = []
    # head = None
    # for val in preorder:
    #     if not head:
    #         head = TreeNode(val)
    #         stack.append(head)
    #     else:
    #         node = TreeNode(val)
    #         if idx[val] < idx[stack[-1].val]:
    #             stack[-1].left = node
    #         else:
    #             while stack and idx[stack[-1].val] < idx[val]:
    #                 u = stack.pop()
    #             u.right = node
    #         stack.append(node)
    # return head

    '''
        1
    2       3

    inorder: [2,1,3]
    preordeR: [1,2,3]

    solve the problem using subproblems... 
    constructs the root using preorder 
    constructs the left and right subtrees by finding smaller subtrees
    
    '''
    if inorder and preorder:
        popped = preorder.pop(0)
        root = TreeNode(popped)
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root
    return None
