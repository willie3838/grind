
'''
TC: O(2^n * n)
'''
def generateParenthesis(n):
    res = []
    helper(n, 0, 0, "", res)
    return res

def helper(n, left, right, path, res):
    if (left+right)//2 > n:
        return
    if (left+right)//2 == n and isMatch(path):
        res.append(path)
        return

    if left <= right:
        helper(n, left+1, right, path+"(", res)
    else:
        helper(n, left+1, right, path+"(", res)
        helper(n, left, right+1, path+")", res)


def isMatch(path):
    left = 0
    for char in path:
        if char == "(":
            left += 1
        elif char == ")" and left == 0:
            return False
        elif char == ")":
            left -= 1
    return True if left == 0 else False


print(generateParenthesis(3))


