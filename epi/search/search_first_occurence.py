
'''

[1,1,2,3]

'''
def search(arr, target):
    l,r = 0, len(arr)-1
    ans = -1
    while l <= r:
        mid = (l+r)//2

        if target > arr[mid]:
            l = mid + 1
        elif target < arr[mid]:
            r = mid
        else:
            ans = mid
            r = mid - 1
    return ans


print(search([1,2,3,3], 3))