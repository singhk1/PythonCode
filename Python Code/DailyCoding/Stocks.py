def maxProfit(prices):
    max_total_profit = 0
    first_profits = [0]*len(prices)
    min_price = float('inf')

    # Forward phase
    for i in range(len(prices)):
        min_price = min(min_price, prices[i])
        profit = prices[i] - min_price
        max_total_profit = max(max_total_profit, profit)
        first_profits[i] = max_total_profit

    max_price = float('-inf')

    # Backward phase
    for j in reversed(range(len(prices))):
        max_price = max(max_price, prices[j])
        profit = max_price - prices[j]
        max_total_profit = max(max_total_profit, first_profits[j-1] + profit)

    return max_total_profit

prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))
