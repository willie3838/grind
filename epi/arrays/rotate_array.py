'''
Even case:
[1,2]
[3,4]

[1, 2, 3, 4]
[5, 6, 7, 8]
[9,10,11,12]
[13,14,15,16]
- rotate by layers

Odd case:
[1,2,3]
[4,5,6]
[7,8,9]
- rotate by layers but one thing remaining in the center


'''

def rotate(arr):
    top = 0
    left = 0
    right = len(arr[0])-1
    bot = len(arr)-1

    while top < bot and left < right:
        for i in range(right-left):
            tmp = arr[top][left+i]
            arr[top][left+i] = arr[bot-i][left]
            arr[bot-i][left] = arr[bot][right-i]
            arr[bot][right-i] = arr[top+i][right]
            arr[top+i][right] = tmp

        top += 1
        bot -= 1
        left += 1
        right -= 1
    return arr

print(~1)
print(rotate(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
))

'''
[7,2,1]
[4,5,6]
[9,8,3]

[7,4,1]
[8,5,2]
[9,6,3]

[7,4,1]
[8,5,2]
[9,6,3]

'''
