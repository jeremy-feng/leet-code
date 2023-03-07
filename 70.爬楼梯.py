#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        a, b, c = 1, 2, 3
        for _ in range(3, n):
            a, b = b, c
            c = a + b
        return c


# @lc code=end
