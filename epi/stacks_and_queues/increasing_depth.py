class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

'''
    1
   2  3

'''
import collections

def levelOrder(root):
    curr = collections.deque()
    res = []

    curr.appendleft(root)

    while curr:
        level = []
        for _ in range(len(curr)):
            if curr[-1].left:
                curr.appendleft(curr.left)
            if curr[-1].right:
                curr.appendleft(curr.right)
            level.append(curr.pop().val)
        res.append(level)
    return res
    # curr = [root]
    # res = []

    # # TC: O(n) because we'll go through every single node in the tree in all cases
    # # SC: O(n)
    # while curr:
    #     res.append([node.val for node in curr])

    #     level = []
    #     for node in curr:
    #         if node.left:
    #             level.append(node.left)
    #         if node.right:
    #             level.append(node.right)
    #     curr = level
    
    # return res

        