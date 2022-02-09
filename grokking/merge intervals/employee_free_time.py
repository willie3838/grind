'''
Problem Challenge 3

Employee Free Time (hard)
For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. 
Our goal is to find out if there is a free interval that is common to all employees. 
You can assume that each list of employee working hours is sorted on the start time.

Example 1:
Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employess are free between [3,5].

Example 2:
Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employess are free between [4,6] and [8,9].

Example 3:
Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employess are free between [5,7].
'''
'''
[1,3], [2,4], [6,8], [9,12]
'''
def freeTime(hours):
    all = []
    # O(n*k)
    for h in hours:
        all.extend(h)
    
    res = []
    # O( (n*k) log (n*k))
    all.sort()
    prevEnd = all[0][1]

    # O(n*k)
    for h in all:
        if h[0] > prevEnd:
            res.append([prevEnd, h[0]])
        prevEnd = max(prevEnd, h[1])
    return res
    # tmp1= []
    # # O(n x k)
    # for i in range(len(hours)):
    #     for h in hours[i]:
    #        tmp1.append(h)
    
    # # O((n*k) log (n*k))
    # tmp1.sort()

    # tmp2 = []

    # # O (n*k)
    # for h in tmp1:
    #     if not tmp2 or h[0] > tmp2[-1][1]:
    #         tmp2.append(h)
    #     else:
    #         tmp2[-1][0] = min(tmp2[-1][0], h[0])
    #         tmp2[-1][1] = max(tmp2[-1][1], h[1])
    # res = []
    
    # # O(n*k)
    # for i in range(1, len(tmp2)):
    #     res.append([tmp2[i-1][1], tmp2[i][0]])
    # return res

print(freeTime([[[1,3]], [[2,4]], [[3,5], [7,9]]]))
print(freeTime([[[1,3], [9,12]], [[2,4]], [[6,8]]]))