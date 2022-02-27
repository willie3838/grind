
'''

99
'''
def increment(arr):
    carry = 1
    i = len(arr)-1

    # while we have a carry and aren't out of bounds
    # add it through the digits
    while carry and i >= 0:
        summ = arr[i] + carry
        if summ > 9:
            arr[i] = summ % 10
        else:
            arr[i]  = summ
            carry = 0
        i -= 1
    # the case if all digits are 9s so we replace the first digit with 1
    # and add the 0 to the end
    # ex: 999 -> 1000
    if carry == 1:
        arr[0] = carry
        arr.append(0)

    return arr

print(increment([1,2,9]))