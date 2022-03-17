'''
Hello world!

e lHlowrdlo!

TC: O(n)
SC: O(n)
'''
def sinusoidal(s):


    # Brute Force
    # TC: O(n)
    # SC: O(n)
    res = [[None]*len(s) for _ in range(3)]
    row = 1
    col = 0
    step = -1

    for i in range(len(s)):
        res[row][col] = s[i]

        if row == 0:
            step = 1
        elif row == 2:
            step = -1
        
        row += step
        col += 1
    
    ans = ""
    for i in range(len(res)):
        for j in range(len(res[0])):
            if res[i][j]:
                ans += res[i][j]
    return ans


    # tmp = [""]*3
    # index = 1
    # step = -1
    # for i in range(len(s)):
    #     tmp[index] += s[i]
    #     if index == 2:
    #         step = -1
    #     elif index == 0:
    #         step = 1
    #     index += step
   
    # return "".join(tmp)
    

    # res = ""

    # # gets everything at the peak
    # for i in range(1,len(s),4):
    #     res += s[i]
    
    # # gets everything at the middle
    # for i in range(0,len(s),2):
    #     res += s[i]
    
    # # gets everything at the trough
    # for i in range(3, len(s), 4):
    #     res += s[i]
    
    # return res

print(sinusoidal("Hello world!"))