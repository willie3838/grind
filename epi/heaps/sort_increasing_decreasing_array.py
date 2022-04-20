'''
[5,3,2,1,100,1000]


TC: O(n log k)
SC: O(k)
'''

import heapq
def sortIncreasingDecreasing(A):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0


    # creates an array to all sorted arrays in increasing order
    for i in range(1, len(A) + 1):
        if i == len(A) or (A[i-1] < A[i] and subarray_type == DECREASING)\
        or (A[i-1] >= A[i] and subarray_type == INCREASING):
            sorted_subarrays.append(A[start_idx:i]) if INCREASING else A[start_idx:i][::-1]
            start_idx = i
            subarray_type = DECREASING if subarray_type == INCREASING else INCREASING
    

    # stores the iterators
    iterators = [iter(arr) for arr in sorted_subarrays]
    min_heap = []

    for i,it in enumerate(iterators):
        heapq.heappush(min_heap, (next(it, None), i))
    
    res = []
    while min_heap:
        smallest, smallest_i = heapq.heappop(min_heap)
        res.append(smallest)
        iter = iterators[smallest_i]
        nextt = next(iter, None)
        if nextt:
            heapq.heappush(min_heap, (nextt, smallest_i))

    return res

        
    


    
