import heapq

'''

        10
    5       20
        15     30

'''
def findKLargest(root, k):
    res = []
    helper(root, k, res)
    return res


def helper(root, k, res):
    if not root or len(res) >= k:
        return None
    
    helper(root.right, k, res)
    if len(res) < k:
        res.append(root.val)
        helper(root.left, k, res)