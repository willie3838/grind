


'''

[0,5.8]


[-2,0,2,3]

TC: logn
SC: 1
'''
def search(arr):
    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            r = mid - 1
        else:
            l = mid + 1
    return -1

print(search([-2,0,2,3]))
print(search([0,5,8]))
print(search([-2,0,2,3,6,7,9]))