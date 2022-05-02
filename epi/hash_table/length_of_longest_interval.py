
def longestLengthofInterval(arr):
    # arr.sort()
    freq = set(arr)
    res = 1

    while freq:
        curr = freq.pop()
        length = 1

        while curr+1 in freq:
            length += 1
            curr = curr + 1
        
        while curr-1 in freq:
            length += 1
            curr = curr - 1
        
        res = max(res, length)
    
    return res
        



print(longestLengthofInterval([3,-2,7,9,8,1,2,0,-1,5,8]))
'''
-2,-1,0,1,2,3,5,7,8,8,9

'''