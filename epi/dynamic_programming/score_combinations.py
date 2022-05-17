'''


dp = [0,0,1,1,1,1,0,0,0,0,0,0,0]

'''
def numberOfCombinations(points):
    plays = [2,3,7]
    dp = [[1] + [0]*points for _ in plays]
    
    for i in range(len(dp)):
        for j in range(1, len(dp[0])):
            withPlay = dp[i][j-plays[i]] if j >= plays[i] else 0
            withoutPlay = dp[i-1][j] if i >= 1 else 0
            dp[i][j] = withPlay + withoutPlay
    return dp[-1][-1]

print(numberOfCombinations(12))