def isHere(arr, target):
    
    # TC: O(n log m)
    for i in range(len(arr)):
        l,r = 0, len(arr[0])-1

        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
    return False

    
    # TC: O(n + m) where n is the number of rows and m is the number of columns
    # each step we eliminate either a row or column
    i = 0
    j = len(arr[0]) - 1

    while i < len(arr) and j >= 0:
        if target == arr[i][j]:
            return True
        elif target > arr[i][j]:
            i += 1
        else:
            j -= 1
    return False


arr = [
    [-1,2,4,4,6],
    [1,5,5,9,21],
    [3,6,6,9,22],
    [3,6,8,10,24],
    [6,8,9,12,25],
    [8,10,12,13,40]
]

print(isHere(arr, 0))