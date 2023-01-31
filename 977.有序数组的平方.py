#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_idx = 0
        right_idx = size - 1
        result = []
        while left_idx <= right_idx:
            # 若第 1 个元素的绝对值小于等于最后一个元素的绝对值
            if abs(nums[left_idx]) <= abs(nums[right_idx]):
                # 则最后一个元素的平方最大，应放到新数组的最后
                # 这里先 append ，之后会反转
                result.append(nums[right_idx]**2)
                # 将 right_idx 向左移动
                right_idx = right_idx - 1
            # 若第 1 个元素的绝对值大于最后一个元素的绝对值
            else:
                # 则第 1 个元素的平方最大，应放到新数组的最后
                # 这里先 append ，之后会反转
                result.append(nums[left_idx]**2)
                # 将 left_idx 向右移动
                left_idx = left_idx + 1
        # 将 result 反转
        return result[::-1]

# @lc code=end

"""
双指针法：平方后最大的数，在平方前一定是最大的正数，或最小的负数。因此，原数组的第 1 个元素和最后一个元素平方后才有可能是最大的数。
"""