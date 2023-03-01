#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # 直接用库函数，记得要对 s[:] 赋值，而不是直接赋值给 s
        # s[:] = s[::-1]
        # 双指针法
        l = 0
        r = len(s) - 1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1


# @lc code=end
