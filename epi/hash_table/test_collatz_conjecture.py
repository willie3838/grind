def testConjecture(n):
    verified = set()
    for i in range(1, n+1):
        k = i
        visited = set()
        while k != 1:
            if k in verified:
                break
            if k in visited:
                return False
            visited.add(k)
            if k%2 == 0:
                k = k/2
            else:
                k = k*3+1
        verified.add(i)
    

    return True
