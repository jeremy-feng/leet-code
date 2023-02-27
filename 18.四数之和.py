#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 先将 nums 排序
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j >= i + 2 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ < target:
                        l += 1
                    elif sum_ > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l != r and nums[l] == nums[l + 1]:
                            l += 1
                        while l != r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


# @lc code=end
