#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        # 初始化 dp 数组
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包容量
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        # 判断是否能凑成总金额
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]


solution = Solution()
solution.coinChange(coins=[1, 2, 5], amount=11)

# @lc code=end
