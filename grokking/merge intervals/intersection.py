'''
Problem Statement 
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Example 1:
Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''
'''

[2,2], [2,3]
'''

def intersection(interval1, interval2):
    res = []
    i = 0
    j = 0

    while i < len(interval1) and j < len(interval2):
        x = max(interval1[i][0], interval2[j][0])
        y = min(interval1[i][1], interval2[j][1])

        if x <= y:
            res.append([x,y])

        if interval2[j][1] < interval1[i][1]:
            j += 1
        else:
            i += 1
    return res
        


        
        

        

print(intersection([[1, 3]], [[3, 5]]))
print(intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
print(intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))