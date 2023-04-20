#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1 for _ in range(n + 1)]
        dp[0] = 0
        # 遍历物品
        for i in range(1, int(n**0.5) + 1):
            # 正序遍历背包容量
            for j in range(i**2, n + 1):
                dp[j] = min(dp[j], dp[j - i**2] + 1)
        return dp[-1]


# @lc code=end
