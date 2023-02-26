#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_1 = {}
        for num in list(set(nums1)):
            dict_1[num] = 1
        result = []
        for num in list(set(nums2)):
            if num in dict_1:
                result.append(num)
                dict_1.pop(num)
        return result


# @lc code=end
