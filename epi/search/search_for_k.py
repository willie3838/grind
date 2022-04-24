import bisect
'''

[1,3] lookg for 2

TC: O(log n)
SC: O(1)
'''
def searchForK(arr, k):
    l,r = 0, len(arr)-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == k:
            ans = mid
            r = mid-1
        elif k < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return ans


    # while l < r:
    #     # no overflow bc python has no limit for its integer
    #     mid = (l+r)//2

    #     if arr[mid] < k:
    #         l = mid + 1
    #     else:
    #         r = mid
    # return l if arr[l] == k else -1


    # # cheating way
    # i = bisect.bisect_left(arr, k)
    # return i if i != len(arr) else -1



print(searchForK([-14,-10,2,108,108,243,285,285,285,401], 285))