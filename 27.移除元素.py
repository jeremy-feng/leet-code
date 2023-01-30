#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        fast = 0
        slow = 0
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        return slow
# @lc code=end

"""
双指针，用图像理解。https://code-thinking.cdn.bcebos.com/gifs/27.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0-%E5%8F%8C%E6%8C%87%E9%92%88%E6%B3%95.gif
"""