#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 创建无穷大的数
        result = float("inf")
        start = 0
        sum = 0 
        for end in range(len(nums)):
            sum = sum + nums[end]
            while sum >= target:
                # 当找到一个连续子数组，满足其和 ≥ target 时，可以将当前的数组长度与之前的最优数组长度进行比较，取最小值
                result = min(result, end - start + 1)
                # 由于目前满足 sum ≥ target ，可以将左指针向右移动一格
                sum = sum - nums[start]
                start = start + 1
        if result == float("inf"):
            return 0
        else:
            return result
# @lc code=end
"""
双指针法。解析：https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md
"""
