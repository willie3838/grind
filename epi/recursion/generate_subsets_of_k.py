'''
TC: O(k*2^k)
SC: O(k)
'''
def generateSubset(k, n):
    res = []
    arr = [i for i in range (1,n+1)]
    helper(k, arr, 0, [], res)
    return res

def helper(k, arr, i, path, res):
    if i >= len(arr) or len(path) > k:
        return
    if len(path)==k:
        res.append(path)
        return
    
    helper(k, arr, i+1, path + [arr[i]], res)
    helper(k, arr, i+1, path, res)


print(generateSubset(2,5))
    