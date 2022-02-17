'''
Problem Statement 
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''
'''
        1
    2       3
 5    6   7   8

[[1],[2,3],[5,6,7,8]]

TC: O(n)
SC: O(n)
'''

from collections import deque
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def levelOrder(root):
    if not root:
        return []

    q = deque()
    q.appendleft(root)
    res = []
    while q:
        level = []
        res.append([x.val for x in q])
        for node in q:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        q = level
    return res

root = Node(1)

root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(6)

root.right = Node(3)
root.right.left = Node(7)
root.right.right = Node(8)

print(levelOrder(root))