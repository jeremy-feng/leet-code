#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        count = 0
        # 先计算 nums1 和 nums2 的所有可能的和，及其出现的次数
        two_sum = dict()
        for num1 in nums1:
            for num2 in nums2:
                two_sum[num1 + num2] = two_sum.get(num1 + num2, 0) + 1
        # 若 -num3 - num4 出现在 two_sum 中，则说明可以组成 two_sum[-num3 - num4] 次
        for num3 in nums3:
            for num4 in nums4:
                if -num3 - num4 in two_sum:
                    count += two_sum[-num3 - num4]
        return count


# @lc code=end
