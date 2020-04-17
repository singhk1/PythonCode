def max_profit(prices, fee):
    n = len(prices)
    if n < 2:
        return 0

    buy = [0] * n
    sell = [0] * n
    buy[0] = -prices[0] - fee

    for i in range(1, n):
        buy[i] = max(buy[i - 1], sell[i - 1] - prices[i] - fee)
        sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

    return sell[-1]

def max_profit_with_optimized_Space(prices, fee):
    n = len(prices)
    if n < 2:
        return 0

    buy = -prices[0] - fee
    sell = 0
    for i in range(1, n):
        last_buy = buy
        buy = max(buy, sell - prices[i] - fee)
        sell = max(sell, last_buy + prices[i])
    return sell


prices = [1, 3, 2, 8, 4, 10]
fee = 2
print(max_profit(prices, fee))
print(max_profit_with_optimized_Space(prices, fee))
