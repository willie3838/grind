

'''
  0 1
 [1,2]
  0 1
 [1,2]
'''

from collections import deque
def multiply(num1, num2):
    # sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    # num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    # # at most, we'll have n+m digits in the product
    # # proof: 10 x 100 = 1000 -> smallest 2 and 3 digit numbers -> only need 4 digits when n+m = 5
    # # 99 x 999 = 98901 -> largest 2 and 3 digit numbers -> need 5 digits and n+m = 5
    # result = [0] * (len(num1) + len(num2))

    # for i in reversed(range(len(num1))):
       
    #     for j in reversed(range(len(num2))):
    #         print(result, i, j)
    #         result[i+j+1] += num1[i] * num2[j]
    #         result[i+j] += result[i+j+1]//10
    #         result[i+j+1] %= 10

    # result = result[next((i for i,x in enumerate(result) if x != 0),len(result)):] or [0]
    # return [sign * result[0]] + result[1:]

    sign = -1 if (num1[0] & 1) ^ (num2[0] & 1) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    res = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            res[i+j+1] = num1[i]*num2[j]
            res[i+j] = res[i+j+1]//10
            res[i+j+1] %= 10

    res= res[next((i for i,x in enumerate(res) if x!= 0), len(res)):] or [0]
    return [res[0]*sign] + res[1:]

    # '''
    # MY CODE -> BRUTE FORCE MULTIPLY NUMBERS, STORE THE PRODUCTS, SUM THEM UP
    # The TC is ass and space as well ~ quadratic time and quadratic space
    # '''
    # res = []
    # for i in reversed(range(len(num1))):
    #     tmp = deque()
    #     carry = 0

    #     x = i
    #     while x < len(num1)-1:
    #         tmp.appendleft(0)
    #         x += 1
        
    #     for j in reversed(range(len(num2))):
    #         product = num1[i] * num2[j] + carry
    #         if product > 9:
    #             carry = product // 10
    #         else:
    #             carry = 0
    #         tmp.appendleft(product % 10)
    #         print(tmp, i, j)
    #     if carry != 0:
    #         tmp.appendleft(carry)
        
    #     res.append(tmp)
    

    # return res
    
    

res = [0,0,0,0]
res= res[next((i for i,x in enumerate(res) if x!= 0), len(res)):]

# print(multiply([1,2],[1,2]))


