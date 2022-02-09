'''
Problem Challenge 2
Maximum CPU Load (hard)

We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).

Example 2:
Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Example 3:
Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4]. 
'''

# def maxCpuLoad(jobs):
#     jobs.sort()
#     tmp = []
#     res = jobs[0][2]

#     for start,end,load in jobs:
#         if not tmp or start >= tmp[-1][1]:
#             tmp.append([start,end,load])
#         else:
#             tmp[-1][0] = min(start, tmp[-1][0])
#             tmp[-1][1] = max(end, tmp[-1][1])
#             tmp[-1][2] += load

#         res = max(res, tmp[-1][2])
#     return res

import heapq
def maxCpuLoad(jobs):
    jobs.sort()
    res = jobs[0][2]
    curr = 0
    heap = []

    for start,end,load in jobs:
        while len(heap) > 0 and start >= heap[0][1]:
            curr -= heap[0][2]
            heapq.heappop(heap)
        curr += load
        heapq.heappush(heap, [start, end, load])
        res = max(curr, res)
    return res

#   # sort the jobs by start time
#   jobs.sort()
#   max_cpu_load, current_cpu_load = 0, 0
#   min_heap = []

#   for j in jobs:
#     # remove all the jobs that have ended
#     while(len(min_heap) > 0 and j[0] >= min_heap[0][1]):
#       current_cpu_load -= min_heap[0][2]
#       heapq.heappop(min_heap)
#     # add the current job into min_heap
#     heapq.heappush(min_heap, j)
#     current_cpu_load += j[2]
#     max_cpu_load = max(max_cpu_load, current_cpu_load)
#   return max_cpu_load
test = [2,10,42,1]
heapq.heapify(test)
print(test)
print(maxCpuLoad([[1,4,3], [2,5,4], [7,9,6]]))
print(maxCpuLoad([[6,7,10], [2,4,11], [8,12,15]]))
print(maxCpuLoad([[1,4,2], [2,4,1], [3,6,5]]))
print(maxCpuLoad([[1,4,2], [4,7,100], [10,11,5]]))