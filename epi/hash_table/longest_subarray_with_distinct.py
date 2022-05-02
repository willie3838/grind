'''
a,b,c,a,d,e

'''
def lengthOfLongestSubarray(arr):
    start = 0
    visited = set()
    res = 0

    for end in range(len(arr)):
        if arr[end] in visited:
            res = max(res, end-start)
            while arr[start] != arr[end]:
                start += 1
            start += 1
        else:
            visited.add(arr[end])
    return res

