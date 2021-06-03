# Question 2. Given the stock value of VIC in n continuous days as an array, e.g., A = [p1, p2, p3, ..., pn]
# Please find a single buying date and a single selling date so that the the buyer could get the best profit.
# Knowing that you have to buy before selling anything.

def find_date_to_get_best_profit(stock_values: list) -> dict:
    transaction_dates = {}
    if not all(isinstance(stock_value, (int, float)) for stock_value in stock_values):
        print("Invalid input value!")
        raise Exception('Input values should a list of integers!')
    total_stock_dates = len(stock_values)
    if total_stock_dates < 2:
        return transaction_dates
    # Assign the first date to the buying_date and the second date to the selling_date.
    transaction_dates = {
        "buying_date": 1,
        "selling_date": 2
    }
    best_profit = stock_values[1] - stock_values[0]

    for buying_index in range(0, total_stock_dates - 1):
        for selling_index in range(buying_index + 1, total_stock_dates):
            profit = stock_values[selling_index] - stock_values[buying_index]
            if profit > best_profit:
                transaction_dates['buying_date'] = buying_index + 1
                transaction_dates['selling_date'] = selling_index + 1
                best_profit = profit

    return transaction_dates


if __name__ == '__main__':
    stocks = [100, 180, 260, 310, 40, "535", 695.5]
    best_p = find_date_to_get_best_profit(stocks)
    print(best_p)
