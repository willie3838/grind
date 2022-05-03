def merge(arr1, arr2):
    i = j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    
    res += arr1[i:] if i < len(arr1) else []
    res += arr2[j:] if j < len(arr2) else []
    return res
    