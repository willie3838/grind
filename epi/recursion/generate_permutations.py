# TC: O(n!)
# SC: O(n!) <- because we have to store it
def generatePermutations(arr):
    res = []
    helper(arr, [], res)
    return res

def helper(arr, path, res):
    if not arr:
        res.append(path)
        return

    for i in range(len(arr)):
        helper(arr[:i] + arr[i+1:], path + [arr[i]], res)

print(generatePermutations([1,2,3]))