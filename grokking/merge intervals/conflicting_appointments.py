# Problem Statement 
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# Example 2:

# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.

# Example 3:

# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

# TC: O(n log n)
# SC: O(n)

def hasConflict(apps):
    apps.sort(key=lambda x:x[0])


    for i in range(1,len(apps)):
        if apps[i][0] < apps[i-1][1]:
            return False

    return True

print(hasConflict([[4,5], [2,3], [3,6]]))
print(hasConflict([[6,7], [2,4], [8,12]]))
print(hasConflict([[1,4], [2,5], [7,9]]))