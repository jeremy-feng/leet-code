#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化数组
        # 不能用 nums = [[0] * n] * n
        # 上面的代码生成的数组的三个元素是相同的，改变 nums[0][0]，则 nums[1][0] 和 nums[2][0] 都会改变
        nums = [[0] * n for _ in range(n)]
        # 初始化索引
        i = 0
        j = 0
        # 初始化计数
        num = 1
        #  每条边应该到 n - offset 就截止
        offset = 1
        # 每到对角线，视为一圈循环的起始。一共要经过n // 2 次对角线
        for circle in range(1, n // 2 + 1):
            # 从 1 到 3
            while j < n - offset:
                nums[i][j] = num
                j = j + 1
                num = num + 1
            # 从 3 到 4
            while i < n - offset:
                nums[i][j] = num
                i = i + 1
                num = num + 1
            # 从 5 到 6
            while j > offset - 1:
                nums[i][j] = num
                j = j - 1
                num = num + 1
            # 从 7 到 8
            while i > offset - 1:
                nums[i][j] = num
                i = i - 1
                num = num + 1
            # 由于要开始新的一圈，因此 i 需要加 1，以抵消上一步的减 1
            i = i + 1
            # 由于要开始新的一圈，因此 num 需要减 1，以抵消上一步的加 1
            num = num - 1
            # 开始新的一圈
            offset = offset + 1
            print(nums)
        if n % 2 == 1:
            # 3 的中间位置是 nums[1][1]
            middle = (n - 1) // 2
            nums[middle][middle] = n**2
        return nums


# @lc code=end
