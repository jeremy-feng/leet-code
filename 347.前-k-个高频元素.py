#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#


# @lc code=start
class Solution:
    def topKFrequent(self, nums, k: int):
        # # ! 自己手动计数，效率不高！
        # count_dict = {}
        # for i in nums:
        #     count_dict[i] = count_dict.get(i, 0) + 1

        # answer = []
        # for _ in range(k):
        #     max_freq = 0
        #     for i in count_dict.keys():
        #         if count_dict[i] > max_freq:
        #             max_freq = count_dict[i]
        #             current_max_freq_item = i
        #     count_dict[current_max_freq_item] = -1
        #     answer.append(current_max_freq_item)
        # return answer
        # * 使用 collections.Counter，快速计数！
        answer = []
        import collections

        count_dict = collections.Counter(nums)
        topK = count_dict.most_common(k)
        for i in topK:
            answer.append(i[0])
        return answer


# @lc code=end
