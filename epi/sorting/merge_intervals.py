'''

[1,4],[2,7] -> [1,7]


[4,5],[1,3] -> [1,3],[4,5]

TC: O(n log n)
SC: O(n)
'''
def mergeIntervals(arr, interval):
    res = []
    arr.append(interval)
    arr.sort()

    for x,y in arr:
        if res and x <= res[-1][1]:
            res[-1][0] = min(x, res[-1][0])
            res[-1][1] = max(y,res[-1][1])
        else:
            res.append([x,y])
    return res

print(mergeIntervals([[-4,-1],[0,2],[3,6],[7,9],[11,12],[14,17]], [1,8]))
