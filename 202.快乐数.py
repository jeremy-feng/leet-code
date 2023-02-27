#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def sum_of_square(self, n: int) -> int:
        n_string = str(n)
        sum_of_square = 0
        for i in range(len(n_string)):
            sum_of_square += int(n_string[i]) ** 2
        return sum_of_square

    def isHappy(self, n: int) -> bool:
        all_result = []
        sum_of_square = self.sum_of_square(n)
        while sum_of_square not in all_result:
            if sum_of_square == 1:
                return True
            else:
                all_result.append(sum_of_square)
                sum_of_square = self.sum_of_square(sum_of_square)
        return False


# @lc code=end
