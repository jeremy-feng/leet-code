#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        # 遍历物品
        for i in coins:
            # 顺序遍历背包容量
            for j in range(i, amount + 1):
                dp[j] = dp[j] + dp[j - i]
        return dp[-1]


# @lc code=end
