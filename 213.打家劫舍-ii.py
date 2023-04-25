#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_no_ring(nums):
            length = len(nums)
            if length == 1:
                return nums[0]
            elif length == 2:
                return max(nums)
            dp = [0 for _ in range(length + 1)]
            for i in range(1, length + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
            return dp[-1]

        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            return max(
                rob_no_ring(nums[:-1]),
                rob_no_ring(nums[1:]),
            )


# @lc code=end
