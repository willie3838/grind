
'''
        2
    1       3

    target = 2, returns 3
    target = 3, returns float('inf')
    target = 1


TC: O(log n)
sc: O(h)
'''
def findFirstGreater(root, target):
    res = [float('inf')]
    return helper(root, target, res)


def helper(root, target, res):
    if target < root.val:
        return findFirstGreater(root.left, target, [min(res[0], root.val)])
    else:
        return findFirstGreater(root.right, target, res)
    

    