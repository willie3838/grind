from signal import valid_signals


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


'''
    3
1       2


3 -> 1 -> 

'''
def createList(root):
    if not root:
        return None
    if not root.left and not root.right:
        return Node(root.val)
    
    left = createList(root.left)
    right = createList(root.right)

    if left:
        left.next = right

    return left