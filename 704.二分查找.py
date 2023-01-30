#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left_idx = 0
        right_idx = n - 1
        while left_idx <= right_idx:
            middle_idx = int((left_idx + right_idx) / 2)
            middle_num = nums[middle_idx]
            if middle_num == target:
                return middle_idx
            elif middle_num < target:
                left_idx = middle_idx + 1
            else:
                right_idx = middle_idx - 1
        return -1
# @lc code=end

"""
左闭右闭，更新区间时记得要 left_idx = middle_idx + 1，right_idx = middle_idx - 1，直到 left_idx > right_idx 才能跳出循环。
"""