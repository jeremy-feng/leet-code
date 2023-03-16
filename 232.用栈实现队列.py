#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#


# @lc code=start
class MyQueue:
    def __init__(self):
        self.i = []
        self.o = []

    def push(self, x: int) -> None:
        self.i.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if len(self.o) == 0:
            for _ in range(len(self.i)):
                self.o.append(self.i.pop())
        return self.o.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        if len(self.o) == 0:
            for _ in range(len(self.i)):
                self.o.append(self.i.pop())
        return self.o[-1]

    def empty(self) -> bool:
        if len(self.i) == 0 and len(self.o) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
