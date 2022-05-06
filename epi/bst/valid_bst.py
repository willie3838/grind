'''
TC: O(n)
SC: O(h)

'''
def isValidBST(self, root):
    return self.helper(root, float('-inf'), float('inf'))
    
def helper(self, root, leftBound, rightBound):
    if not root:
        return True
    
    if root.val <= leftBound or root.val >= rightBound:
        return False
    
    return self.helper(root.left, leftBound, min(root.val, rightBound)) and self.helper(root.right, max(leftBound, root.val), rightBound)
