

def isValid(arr):
    
    # O(1) since it's always 9x9
    for i in range(len(arr)):
        rows = set()
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                continue
            if arr[i][j] in rows:
                return False
            rows.add(arr[i][j])
    
    # O(1) since it's always 9x9
    for j in range(len(arr[0])):
        cols = set()
        for i in range(len(arr)):
            if arr[i][j] == 0:
                continue
            if arr[i][j] in cols:
                return False
            cols.add(arr[i][j])
    
    # O(1) since it's always 9 x (3x3)
    # for an nxn grid it'd be... O(n^2)
    for y in range(0,len(arr),3):
        for x in range(0, len(arr),3):
            sub = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if arr[i][j] == 0:
                        continue
                    if arr[i][j] in sub:
                        return False
                    sub.add(arr[i][j])
    
    return True

print(isValid(
    [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
))