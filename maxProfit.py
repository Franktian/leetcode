import sys

def maxProfit(prices):
    i = 0
    min_price = sys.maxsize
    max_profit = 0
    
    while i < len(prices):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        i += 1
    return max_profit