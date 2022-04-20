import heapq



'''
TC: O(n log k) where k is the number of lists and n is the number of elements
SC: O(n)


Input: [ [2,3,5], [0,1], [4,5,6] ]
Output: [0,1,2,3,4,5,6]
'''
def mergeFiles(files):

    # res = []
    # for file in files:
    #     for time in file:
    #         heapq.heappush(res, time)
    # return res

    min_heap = []
    iterators = [iter(file) for file in files]

    for i, it in enumerate(iterators):
        first = next(it, None)
        if first is not None:
            heapq.heappush(min_heap, (first, i))
    
    res = []
    while min_heap:
        smallest, smallest_i = heapq.heappop(min_heap)
        res.append(smallest)

        nextt = next(iterators(smallest_i), None)
        if nextt is not None:
            heapq.heappush(min_heap, (nextt, smallest_i))

    return res