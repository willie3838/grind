
def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x = abs(x)
    
    # O(n)
    res = list(str(x))
    start, end = 0, len(res)-1

    # O(n)
    while start < end:
        res[start], res[end] = res[end], res[start]
        start += 1
        end -= 1
    return "".join(res) if not negative else "-"+"".join(res)

print(reverse(-123))
