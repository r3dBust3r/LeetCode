# Name: best-time-to-buy-and-sell-stock
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ISSUE: Time Limit Exceeded


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit


print(
    Solution.maxProfit(
        None,
        [
            905,510,174,329,873,382,
            279,855,396,810,322,192,
            442,775,445,861,303,980,
            478,543,87,875,283,740,
            376,156,654,230,392,190
        ]
    )
)
