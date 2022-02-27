
'''
3 pointers
- left = location of the last element less than pivot
- right = location of the last element greater than or equal to the pivot
- everything in between = unknown

'''



'''
pivot = 3
[3,1,3,1,2]

'''
def partition(arr, p):
    # smaller = 0
    # for i in range(len(arr)):
    #     if arr[i] < p:
    #         arr[i], arr[smaller] = arr[smaller], arr[i]
    #         smaller += 1

    left, right = 0, len(arr)-1
    while left < right:
        if arr[left] >= p:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        else:
            left += 1
    return arr

    # left, equal, right = 0, 0, len(arr)-1
    # while equal <= right:
    #     # the case that we find an element greater than or equal to the pivot
    #     # we place it at the right index and update it
    #     # we don't update the left index because we don't know what swapped into it
    #     if arr[equal] > p:
    #         arr[equal], arr[right] = arr[right], arr[equal]
    #         right -= 1
    #     elif arr[equal] == p:
    #         equal += 1
    #     else:
    #         arr[equal], arr[left] = arr[left], arr[equal]
    #         left += 1
    #         equal += 1
    # return arr


print(partition([0,1,2,0,2,1,1], 2))

'''

0,1,2,0,2,1,1
0,1,0,2,2,1,1
0,1,0,2,2,1
'''