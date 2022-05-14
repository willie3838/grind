'''

'''
def generatePalindromicDecomp(s):
    res = []
    helper(s, [], res)
    return res

def helper(s, path, res):
    if not s:
        res.append(path)
        return
    for i in range(len(s)):
        if s[:i+1] == s[:i+1][::-1]:
            helper(s[i+1:], path+[s[:i+1]], res)


print(generatePalindromicDecomp("0204451881"))