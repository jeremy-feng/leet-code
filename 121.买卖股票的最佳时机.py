#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        # length = len(prices)
        # dp = [0 for _ in range(length)]
        # min_price = float("inf")
        # for i in range(1, length):
        #     min_price = min(min_price, prices[i - 1])
        #     dp[i] = max(dp[i - 1], prices[i] - min_price)
        # return dp[-1]

        # # 动态规划
        # length = len(prices)
        # # dp 是 length * 2 的数组。第 1 列代表持有股票时，最多能有多少现金；第 2 列代表不持有股票时，最多能有多少现金
        # dp = [[0 for _ in range(2)] for _ in range(length)]
        # # 最开始时，持有股票，只能通过买入，那么需要支付第一天的股票价格
        # dp[0][0] = -prices[0]
        # for i in range(1, length):
        #     # 第 i 天时持有股票的成本，要看第 i - 1 天时持有股票的成本，和第 i 天的股票价格中较小的那一个
        #     dp[i][0] = max(dp[i - 1][0], -prices[i])
        #     # 第 i 天时不持有股票的成本，要看第 i - 1 天时不持有股票的现金（之所以第 i - 1 天时不持有股票有现金，是因为第 i - 1 天或更早之前已经出现了卖出股票的行为），和第 i 天卖出股票所得的现金
        #     dp[i][1] = max(dp[i - 1][1], prices[i] + dp[i - 1][0])
        # return dp[-1][1]

        # 动态规划，只保留两个量，分别是持有股票和持有现金
        length = len(prices)
        dp = [-prices[0], 0]
        for i in range(1, length):
            dp[1] = max(dp[1], prices[i] + dp[0])
            dp[0] = max(dp[0], -prices[i])
        return dp[1]


# @lc code=end
