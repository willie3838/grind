'''
Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
'''

def merge(intervals):
    res = []
    intervals.sort()
    for x,y in intervals:
        if not res or x > res[-1][1]:
            res.append([x,y])
        else:
            res[-1][0] = min(x, res[-1][0])
            res[-1][1] = max(y, res[-1][1])
    return res