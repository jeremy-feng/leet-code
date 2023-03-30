#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#


# @lc code=start
class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # 初始化二维数组 dp
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # 遍历物品
        for i in strs:
            # 计算 i 中字符 0 的个数
            num_0 = sum([1 - int(num) for num in i])
            # 计算 i 中字符 1 的个数
            num_1 = sum([int(num) for num in i])
            # 遍历 dp 的行
            for j in range(m, num_0 - 1, -1):
                # 遍历 dp 的列
                for k in range(n, num_1 - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - num_0][k - num_1] + 1)
        return dp[m][n]


solution = Solution()
solution.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)

# @lc code=end
