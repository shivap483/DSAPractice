def get_max_profit(stock_prices):
    if len(stocks) < 2:
        raise ValueError("minimum 2 inputs")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for current_price in stock_prices[1:]:
        potential_profit = current_price - min_price
        min_price = min(min_price, current_price)
        max_profit = max(potential_profit, max_profit)

    return max_profit


stocks = [5, 7, 8, 9, 10, 11]
print(get_max_profit(stocks[::-1]))
