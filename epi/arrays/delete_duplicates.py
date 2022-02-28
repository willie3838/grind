

def deleteDuplicates(arr):
    i = 1
    srted = 1

    # O(n) b/c we'll only go through each element once
    while i < len(arr):
        while i < len(arr) and arr[i] == arr[i-1]:
            i += 1
        if i >= len(arr):
            break
        arr[srted] = arr[i]
        srted += 1
        i += 1
    return arr[:srted]

print(deleteDuplicates([2,3,5,5,7,11,11,11,13]))
print(deleteDuplicates([1,1,1,1]))
