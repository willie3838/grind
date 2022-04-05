

cases = int(input())
c = m = y = k = float('inf')
case_number = 1

for case in range(cases*3):
    carts = input().split()


    c = min(c, int(carts[0]))
    m = min(m, int(carts[1]))
    y = min(y, int(carts[2]))
    k = min(k, int(carts[3]))

    if (case+1)%3 == 0:
        if c > 10**6:
            print("Case #{}: {} {} {} {}".format(case_number, 10**6, 0 , 0, 0))
        elif c+m > 10**6:
            print("Case #{}: {} {} {} {}".format(case_number, c, 10**6-c , 0, 0))
        elif c+m+y > 10**6:
            print("Case #{}: {} {} {} {}".format(case_number, c,  m, 10**6-c-m, 0))
        elif c+m+y+k > 10**6:
            print("Case #{}: {} {} {} {}".format(case_number, c, m , y, 10**6-c-m-y))
        elif c+m+y+k == 10**6:
            print("Case #{}: {} {} {} {}".format(case_number, c, m , y, k))
        else:
            print("Case #{}: IMPOSSIBLE".format(case_number))
        case_number += 1
        c = m = y = k = float('inf')
        



