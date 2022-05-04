
'''
[1,2,5]

'''
def findSmallest(change):
    change.sort()
    minn = 0
    for num in change:
        if num > minn + 1:
            break
        minn += num
    return minn + 1

