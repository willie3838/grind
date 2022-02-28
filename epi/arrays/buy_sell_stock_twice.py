'''
[5,6,10]
6 -> 10 = 4
5-> 10 = 5

note that selling once can be more profitable than selling twice

[1,2,1,10]
1->2 = 1
1->10 = 9

1+9 = 10

2 cases
- we buy twice: [1,2,1,10]
- we buy once: [1,2,3,10,100]
'''

def profit(arr):
    max_total_profit, min_price_so_far = 0, float('inf')
    first_buy_sell_profits = [0] * len(arr)

    for i, price in enumerate(arr):
        min_price_so_far = min(price, min_price_so_far)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit
    
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(arr[1:],1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit, 
            max_price_so_far - price + first_buy_sell_profits[i-1])
    
    return max_total_profit
