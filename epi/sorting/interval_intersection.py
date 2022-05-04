'''

[1,3],
[4,5],


'''
def intervalIntersection(intervals1, intervals2):
    res = []
    i = 0
    j = 0

    while i < len(intervals1) and j < len(intervals2):
        x = max(intervals1[i][0], intervals2[j][0])
        y = min(intervals1[i][1], intervals2[j][1])
        if x <= y:
            res.append([x,y])
        
        if intervals1[i][1] < intervals2[j][1]:
            i += 1
        else:
            j += 1


    return res

print(intervalIntersection(
    [[1,4]],
    [[1,3]]
))