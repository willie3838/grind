
'''

[0,1,2,2] missing = 3, duplicate = 2
'''
def findDuplicateAndMissing(arr):

    # TC: O(2n)
    # SC: O(n)
    all = set()
    duplicate = -1

    for i in range(len(arr)):
        if arr[i] not in all:
            all.add(arr[i])
        else:
            duplicate = arr[i]
    
    for n in range(len(arr)):
        if n not in all:
            return (n, duplicate)


hashh = {}
arr = [0,1]
hashh[arr] = 1
print(hashh)
print(findDuplicateAndMissing([0,1,2,2]))
