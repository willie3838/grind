import heapq

def kLargest(heap, k):
    res = []
    max_heap = []

    heapq.heappush(max_heap, (-heap[0], 0))

    # SC: O(k)
    # TC: O(k log k)
    while max_heap and len(res) < k:
        node,i = heapq.heappop(max_heap)
        res.append(-node)

        if i*2+1 < len(heap):
            heapq.heappush(max_heap, (-heap[i*2+1], (i*2+1)))
        if i*2+2 < len(heap):
            heapq.heappush(max_heap, (-heap[i*2+2], (i*2+2)))
    return res




'''

[561]
[314,401]
[314,359,271]
[314,271]
[271, 156, 28]
'''

print(kLargest([561, 314, 401, 28, 156, 359, 271, 11, 3], 4))