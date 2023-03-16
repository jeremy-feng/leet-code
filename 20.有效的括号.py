#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif c == ")":
                if len(stack) == 0:
                    return False
                elif stack[-1] == ")":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "}":
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if len(stack) == 0:
                    return False
                elif stack[-1] == "]":
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True


# @lc code=end
