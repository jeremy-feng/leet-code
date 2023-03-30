#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#


# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones) -> int:
        # 求所有石头重量之和
        total_sum = sum(stones)
        # 目标是让背包中的物品重量之和尽量接近 total_sum / 2
        # 因此背包容积为 total_sum / 2
        c = int(total_sum / 2)
        # 初始化背包
        dp = [0 for _ in range(c + 1)]
        # 遍历物品
        for i in stones:
            # 倒序遍历背包容积
            for j in range(c, i - 1, -1):
                dp[j] = max(dp[j], dp[j - i] + i)
        return total_sum - 2 * dp[c]


solution = Solution()
solution.lastStoneWeightII([2, 7, 4, 1, 8, 1])

# @lc code=end
