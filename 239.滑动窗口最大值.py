#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        # ! 使用 list 的复杂度太高，会超时
        # answer = []
        # stack = nums[: k - 1]
        # for i in range(k - 1, len(nums)):
        #     stack.append(nums[i])
        #     answer.append(max(stack))
        #     stack = stack[1:]
        # return answer
        # * 使用 deque 数据结构，可以在首尾两端 pop
        # * 参考 https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/hard/239.sliding-window-maximum
        answer = []
        import collections

        q = collections.deque()
        for i in range(len(nums)):
            # q[-1] 这个索引对应的元素小于新进来的元素，则 q[-1] 这个索引对应的元素在未来肯定不是最大值，也就是可以把 q[-1] 这个索引抛出
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            # q[0] 这个索引离当前的 i 太远了，已经不在窗口内了
            while q and q[0] <= i - k:
                q.popleft()
            q.append(i)
            if i >= k - 1:
                answer.append(nums[q[0]])
        return answer


# solution = Solution()
# solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)

# @lc code=end
