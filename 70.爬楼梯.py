#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n
        # 递归
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # 迭代
        # a, b, c = 1, 2, 3
        # for _ in range(3, n):
        #     a, b = b, c
        #     c = a + b
        # return c
        # 完全背包，背包容量为 n
        dp = [0 for j in range(n + 1)]
        dp[0] = 1
        for j in range(n + 1):
            for i in range(1, 2 + 1):
                if i <= j:
                    dp[j] += dp[j - i]
        return dp[n]


# @lc code=end
