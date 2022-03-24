from tkinter import N


n = 10
for i in range(n):
    for j in range(i, n):
        print(i, j)

'''

i = 0, j runs n times
i = 1, j runs n-1 times
i = 2, j runs n-2 times
...
i = n-1, j runs 1 time

'''

