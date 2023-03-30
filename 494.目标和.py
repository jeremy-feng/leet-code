#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 计算数组之和
        total_sum = sum(nums)
        # 计算加号的数字之和
        c = (total_sum + target) / 2
        # c 必须为整数，否则就不存在这样的表达式；total_sum 必须小于 abs(target)，否则就不存在这样的表达式
        if c % 1 != 0 or total_sum < abs(target):
            return 0
        c = int(c)
        # 初始化背包，容量为 c
        # dp[j] 代表装到容量为 j 有几种装法
        dp = [0 for _ in range(c + 1)]
        dp[0] = 1
        # 遍历物品
        for i in nums:
            # 倒序遍历背包容量
            for j in range(c, i - 1, -1):
                dp[j] = dp[j] + dp[j - i]
        return dp[c]


# @lc code=end
