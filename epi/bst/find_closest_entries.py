
# TC: O(n + m + k)
# SC: O(1)

def findClosestEntries(arr1, arr2, arr3):
    i=j=k=0
    minn = float('inf')
    res = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        interval = abs(arr1[i] - arr2[j]) + abs(arr2[j] - arr3[k])
        if interval < minn:
            minn = interval
            res = [arr1[i], arr2[j], arr3[k]]

        if arr1[i] < arr2[j] and arr1[i] < arr3[k]:
            i += 1
        elif arr2[j] < arr1[i] and arr2[j] < arr3[k]:
            j += 1
        elif arr3[k] < arr1[i] and arr3[k] < arr2[j]:
            k += 1
        else:
            return [arr1[i], arr2[j], arr3[k]]

    return res

arr1 = [1,4,5]
arr2 = [2,6,7]
arr3 = [3,8,9]

print(findClosestEntries(arr1,arr2,arr3))