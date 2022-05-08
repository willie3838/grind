'''

Simpler approach

[[3,2,1],[],[]]

Uses the following algorithm
- Move n-1 discs from peg 1 to peg 3 using peg 2
- Moves 1 disc from peg 1 to peg 2
- Moves n-1 discs from peg 3 to peg 2 using peg 1
'''
def towerOfHanoi(n):
    arr = [[] for _ in range(3)]
    for i in range(n, 0, -1):
        arr[0].append(i)
    compute(n, arr, 0, 1, 2)
    print(arr)


def compute(n, arr, initialPeg, targetPeg, usePeg):
    if n <= 0:
        return
    
    compute(n-1, arr, initialPeg, usePeg, targetPeg)
    arr[targetPeg].append(arr[initialPeg].pop())
    print(arr, n)
    compute(n-1, arr, usePeg, targetPeg, initialPeg)

'''

Weird approach

'''
# def move(n):
#     arr = [[] for _ in range(3)]

#     for i in range(n,0,-1):
#         arr[0].append(i)
    
#     place(arr, n)

# def place(arr, n):
#     if len(arr[1]) == n:
#         return
    
#     if arr[1] and not arr[2]:
#         print("Moved ", arr[1], " to peg 3")
#         arr[2] += arr[1]
#         arr[1] = []
#     elif arr[1]:
#         print("Moved ", arr[2], " to peg 2")
#         arr[1] += arr[2]
#         arr[2] = []
    
#     elif not arr[2]:
#         arr[2].append(arr[0].pop())
#         print("Moved ", arr[2][-1], " to peg 3")
#     elif not arr[1]:
#         arr[1].append(arr[0].pop())
#         print("Moved ", arr[1][-1], " to peg 3")

#     print(arr, "\n")
#     place(arr, n)



towerOfHanoi(3)