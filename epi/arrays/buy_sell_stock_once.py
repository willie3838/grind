def profit(arr):
    ans = 0
    # brute force O(n^2)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans = max(arr[j] - arr[i], ans)
    return ans
    # can come to this answer when you realize you only need the curr min
    ans = 0
    currMin = arr[0]
    for num in arr:
        ans = max(num - currMin, ans)
        currMin = min(currMin, num)
    return ans

print(profit([310,315,275,295,260,270,290,230,255,250]))