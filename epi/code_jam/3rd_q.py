cases = int(input())
for caseNumber in range(cases):
    n = int(input())
    dice = input().split()
    for i in range(len(dice)):
        dice[i] = int(dice[i])
    dice.sort()
    maxx = 1

    for i in range(1,len(dice)):
        if dice[i] >= maxx+1:
            print(dice[i], maxx)
            maxx += 1
    print("Case #{}: {}".format(caseNumber+1, maxx))