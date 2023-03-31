#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#


# @lc code=start
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        # 遍历背包容量
        for j in range(target + 1):
            # 遍历物品
            for i in nums:
                if i <= j:
                    dp[j] = dp[j] + dp[j - i]
        return dp[-1]


solution = Solution()
solution.combinationSum4(nums=[1, 2, 3], target=4)

# @lc code=end
