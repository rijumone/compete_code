'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

class Solution:
    def maxProfit(self, prices: list) -> int:
        # print(prices)
        profit = 0
        buy_price = None
        for price_today in prices:
            if buy_price is None:
                buy_price = price_today
                continue
            if price_today < buy_price:
                buy_price = price_today
                continue
            profit_today = price_today - buy_price
            if profit_today > profit:
                profit = profit_today
            # print(profit, profit_today)
        return profit




if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4, ]
    # prices = [7, 6, 4, 3, 1, ]
    profit = Solution().maxProfit(
        prices=prices,
    )
    print(profit)