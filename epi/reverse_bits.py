def swap(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = 1 << i | 1 << j
        x ^= bit_mask
    return x

def reverse(x):
    start = 0
    end = 63
    while start < end:
        swap(x, start, end)
        start += 1
        end -= 1
    return x