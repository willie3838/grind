def findMinMax(arr):
    minn, maxx = float('inf'), float('-inf')
    for num in arr:
        minn = min(num, minn)
        maxx = max(num, maxx)
    
    return (minn, maxx)

print(findMinMax([3,2,5,1,2,4]))

