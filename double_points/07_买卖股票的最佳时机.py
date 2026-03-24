def maxProfit(prices: list[int]) -> int:
    max_pro = 0
    left = 0
    for right in range(1, len(prices)):
        abs_cal = prices[right] - prices[left]
        if abs_cal > max_pro:
            max_pro = abs_cal
        if prices[right] < prices[left]:
            left = right

    return max_pro

prices = [2,1,2,1,0,1,2]
print(maxProfit(prices))



