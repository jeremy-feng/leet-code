#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#


# @lc code=start
class Solution:
    def canPartition(self, nums) -> bool:
        total_sum = sum(nums)
        # 如果总和是奇数，那么一定不能分割为等和子集
        if total_sum % 2 != 0:
            return False
        # 求子集的和
        sub_set_sum = int(total_sum / 2)
        # 背包容积为 sub_set_sum
        # 初始化 dp
        dp = [0 for _ in range(sub_set_sum + 1)]
        # 遍历物品
        for i in nums:
            # 倒序遍历背包容积
            for j in range(sub_set_sum, i - 1, -1):
                dp[j] = max(dp[j], dp[j - i] + i)
            # 如果背包刚好装满了，说明背包内的元素之和等于 sub_set_sum
            if dp[sub_set_sum] == sub_set_sum:
                return True
        return False


solution = Solution()
solution.canPartition([2, 2, 1, 1])

# @lc code=end
