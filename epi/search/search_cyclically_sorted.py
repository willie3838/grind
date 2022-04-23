'''
Algorithm

When an array is cyclically sorted, there are two states:
1. It's not shifted so a[0] < a[-1]. eg: [1,2,3,4,5]
2. It's shifted such that there are two sorted arrays in ascending order. eg: [3,4,5,1,2]

[4,5,1,2,3]


If we're at a position such that A[m] < A[n-1] then we know that anything [m+1, n-1] is not the answer
since A[m] is less than all elements in that range and we want to find the smallest number. Therefore,
we'll stay at the current position and look to the left.

If we're at a position such that A[m] > A[n-1] then we know that the answer is within [m+1, n+1] so we 
want to go to the right subproblem. This is because a cyclically sorted array the lowest element is always
in the second sorted array unless it's in its initial state, but this if condition will never run in that case.
'''
def search(arr):
    l,r = 0, len(arr)-1

    while l < r:
        mid = (l+r)//2
        if arr[mid] < arr[r]:
            r = mid
        else:
            l = mid + 1

       
    return l