def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    n = len(prices)
    for i in range(0, n - 1):
        if prices[i + 1] > prices[i]:
            max_profit += prices[i + 1] - prices[i]
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

