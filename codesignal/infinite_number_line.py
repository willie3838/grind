'''
Given an infinite number line, two types of operations: 
[1, x] - builds an obstacle at coordinate x along the number line. 
It is guaranteed that coordinate x does not contain any obstacles when the operation is performed.
 [2, x, size] - checks whether it's possible to build a block occupying coordinates 
 between x, x + 1, ..., x + size - 1 along the number line. 
 Returns 1 if it is possible, i.e. there are no obstacles at the occupied coordinates, 
 and return 0 otherwise.


  x   x
1 2 3 4 5 6

operations = [ [1,2], [1,4], [2,3,1], [2,4,3] ]
obstacles = [2,4]
output = "10"

'''

import bisect
def blocks(operations):
    obstacles = []
    res = ""
    for operation in operations:
        if operation[0] == 1:
            bisect.insort(obstacles, operation[1])
        else:
            x = operation[1]
            size = operation[2]
            if bisect.bisect_left(obstacles,x) == bisect.bisect_left(obstacles, x-size):
                res += "1"
            else:
                res += "0"
    return res


import heapq
'''

[1,2,3,4]
'''
heap = []
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

print(heap)