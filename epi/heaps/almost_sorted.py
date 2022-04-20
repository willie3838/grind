
import heapq


''''

[3,-1,2,6,5,8]

[-1,2,3]
[2,3,5]
'''
def sortAlmostSorted(arr, k):
    min_heap = []
    res = []

    # TC: O(n log k) where n is the number of elements and k is the most an element will be away from its sorted position
    # SC: O(k)
    for i in range(len(arr)):
        if i < k:
            heapq.heappush(min_heap, arr[i])
        else:
            res.append(heapq.heappushpop(min_heap, arr[i]))
    
    while min_heap:
        res.append(heapq.heappop(min_heap))
    
    return res

print(sortAlmostSorted([3,-1,2,6,5,8], 2))