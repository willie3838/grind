def findIntersection(arr1, arr2):
    i = 0
    j = 0 
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if i == 0 or i > 0 and arr1[i] != arr1[i-1]:
                res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return res


print(findIntersection([2,3,3,5,5,6,7,7,8,12], [5,5,6,8,8,9,10,10]))
