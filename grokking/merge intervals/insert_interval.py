'''
Problem Statement 
Given a list of non-overlapping intervals sorted by their start time,
insert a given interval at the correct position and merge all necessary 
intervals to produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

'''
def insert(intervals, newI):
    res = []
    for x,y in intervals:
        if newI and newI[0] <= y:
            res.append(newI)
            newI = None
        if not res or x > res[-1][1]:
            res.append([x,y])
        else:
            res[-1][0] = min(x, res[-1][0])
            res[-1][1] = max(y, res[-1][1])
    if not res or newI:
        res.append(newI)

    return res

print(insert([[1,3], [5,7], [8,12]], [4,6]))
print(insert([[1,3], [5,7], [8,12]], [4,10]))
print(insert([[2,3], [5,7]],[1,4]))