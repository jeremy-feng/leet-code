#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#


# @lc code=start
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a + b))
            elif i == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a - b))
            elif i == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(a * b))
            elif i == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                # 注意除法，结果有可能不是整数，要将结果转换为 int
                stack.append(str(int(a / b)))
            else:
                stack.append(i)
        return int(stack[0])


# @lc code=end
