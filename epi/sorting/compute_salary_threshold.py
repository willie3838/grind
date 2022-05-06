
# TC: O(n log n) where n is the number of salaries

'''
[1,2,3], target=3, cap=3


[20,30,40,90,100] T=210

salaryCap = 42, salary = 20
salaryCap = 47.5, salary = 30
salaryCap = 53.333, salary = 40
salaryCap = 60, salary = 90
'''
def computeSalaryThreshold(salaries, target):
    salaries.sort()
    cap = target/len(salaries)

    for i,salary in enumerate(salaries):
        if salary <= cap:
            print(cap, salary)
            overAllocated = cap - salary
            remainingSal = (len(salaries)-1)-i
            cap += (overAllocated / remainingSal)
    return cap

print(computeSalaryThreshold([90,30,100,40,20], 210))