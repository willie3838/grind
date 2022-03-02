def next_permutation(arr):
    if len(arr) == 1 or not arr:
            return
        
    i = len(arr)-1
    while i >= 1 and arr[i] <= arr[i-1]:
        i -= 1
    i -= 1
    
    if i == -1:
        return arr.reverse()
    
    minn = float('inf')
    minn_i = 0
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i] and arr[j] <= minn:
            minn = arr[j]
            minn_i = j

    arr[minn_i], arr[i] = arr[i], arr[minn_i]
    arr[i+1:] = reversed(arr[i+1:])

print(next_permutation([1,3,2,4]))
    
