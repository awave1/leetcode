"""
121. Best Time to Buy and Sell Stock
src: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def max_profit_brute_force(prices: list[int]) -> int:
    profit = -float("inf")

    for i, price1 in enumerate(prices):
        for price2 in prices[i + 1 :]:
            potential_profit = price2 - price1
            if potential_profit > profit:
                profit = potential_profit

    return 0 if profit < 0 else profit


def max_profit(prices: list[int]) -> int:
    profit = 0
    current_min_price = prices[0]

    for price in prices[1:]:
        profit = max(profit, price - current_min_price)
        current_min_price = min(current_min_price, price)

    return profit


def test_max_profit_brute_force():
    assert max_profit_brute_force([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit_brute_force([7, 6, 4, 3, 1]) == 0
    assert max_profit_brute_force([2, 4, 1]) == 2


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([2, 4, 1]) == 2
