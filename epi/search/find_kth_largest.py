import random

'''
[1,2,3], k = 2


Average case: O(n) since we'll be splitting the array into halves each time...
Worst case: O(n^2) since we'll consistently pick the largest and we want to find the smallest....
'''
def findKthLargest(arr, k):
    l,r = 0,len(arr)-1

    while l <= r:
        pivot = partition(arr, l, r)
        if len(arr)-pivot == k:
            return arr[pivot]
        elif len(arr)- pivot > k:
            l = pivot + 1
        else:
            r = pivot - 1
    return None

        


def partition(arr, l, r):
    pivot = random.randint(l, r)
    arr[pivot], arr[r] = arr[r], arr[pivot]

    i = l
    for j in range(len(arr)):
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[r], arr[i] = arr[i], arr[r]
    return i
