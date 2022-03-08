
'''
- Always finish top -> right -> bot -> left
- Repeat this but you have to increment your top, right, bot, and left pointers

[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
'''
def spiral(arr):
   
    top = 0
    bot = len(arr)-1
    right = len(arr[0])-1
    left = 0
    res = []
    while top <= bot:

        # get all the top layers
        for i in range(left, right+1):
            res.append(arr[top][i])
        top += 1

        # get all the right layers
        for i in range(top, bot+1):
            res.append(arr[i][right])
        right -= 1

        if top <= bot:
            # get all the bottom layers
            for i in range(right, left-1, -1):
                res.append(arr[bot][i])
            bot -= 1

        if left <= right:
            for i in range(bot, top-1, -1):
                res.append(arr[i][left])
            left += 1

    return res

# print(spiral([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]))

'''
7
9
6
'''
# print(spiral([
#     [1,2],
#     [3,4]
# ]))

# print(spiral([
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]))

arr = [
    [1,2],
    [3,4]
]

'''

[1,2]   [1,3]
[3,4]   [2,4]

'''

res.extend(
            list(zip(*arr))[-1 - x][x:-1 - x]
        )
print(arr, zip(*arr))