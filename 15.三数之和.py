#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        # 存储结果
        res = []
        # 将 nums 排序
        nums.sort()
        for i in range(len(nums) - 2):
            # 如果之前已经有以 i 开头的，那么不需要再以 i 开头了
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # 初始化 l 和 r
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum_ = nums[i] + nums[l] + nums[r]
                if sum_ < 0:
                    l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # 若 l 的下一个数与 l 相同，则可以跳过下一个数
                    while l != r and nums[l] == nums[l + 1]:
                        l += 1
                    # 若 r 的左边一个数与 r 相同，则可以跳过左边一个数
                    while l != r and nums[r] == nums[r - 1]:
                        r -= 1
                    # 由于当前的 i,l 和 r 的和是为 0 的，那么必须同时使 l 增大且 r 减小，才有可能继续保持三数之和为 0。否则，若只增大 l 或减小 r，则不可能继续保持三数之和为 0
                    l += 1
                    r -= 1
        return res


# Solution().threeSum([-1, 0, 1, 2, -1, -4])

# @lc code=end
