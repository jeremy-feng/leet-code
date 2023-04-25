#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [0 for _ in range(length)]
        min_price = float("inf")
        for i in range(1, length):
            min_price = min(min_price, prices[i - 1])
            dp[i] = max(dp[i - 1], prices[i] - min_price)
        return dp[-1]


# @lc code=end
