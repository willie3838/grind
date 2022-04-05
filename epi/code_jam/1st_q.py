cases = int(input())
dimensions = []

for _ in range(cases):
    d = input().split()
    dimensions.append((int(d[0])*2+1, int(d[1])*2+1))


   
for i, (x,y) in enumerate(dimensions):
    print("Case #{}:".format(i+1))
    for row in range(x):
        output = ""
        for col in range(y):
            if (row == 0 or row == 1) and (col == 0 or col == 1):
                output += "."
            elif col%2 == 0:
                if row%2 == 0:
                    output += "+"
                else:
                    output += "|"
            elif col%2 == 1:
                if row%2 == 0:
                    output += "-"
                else:
                    output += "."
        print(output)