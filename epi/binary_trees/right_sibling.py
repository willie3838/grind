from numpy import rot90


class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

'''

        1
    2      3
 4   5   6   7


'''
def createRightSibling(root):
    curr = root
    nextt = root.left

    while nextt:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left
            curr = curr.next
        else:
            curr = nextt
            nextt = curr.left
    return root
    # curr = []
    # curr.append(root)

    # while curr:
    #     level = []
    #     for node in curr:
    #         if node.left:
    #             level.append(node.left)
    #         if node.right:
    #             level.append(node.right)
        
    #     for i in range(1, len(level)):
    #         level[i-1].next = level[i]
        
    #     curr = level
    
    # return root

print((TreeNode(1) and TreeNode(500)).val)