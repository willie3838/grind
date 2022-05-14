
'''
TC: O(n) where n is the number of valid parenthesis 
SC: O(n) where n is the number of valid parenthesis
'''
def generateParenthesis(n):
    res = []
    helper(n, 0, 0, "", res)
    return res

def helper(n, left, right, path, res):
    if right > left or left > n//2:
        return
    if left == n//2 and right == n//2:
        res.append(path)
        return

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


