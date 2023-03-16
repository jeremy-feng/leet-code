#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)


# @lc code=end
