#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash_table = [[0 for i in range(26)] for j in range(len(words))]
        for i, word in enumerate(words):
            for c in word:
                hash_table[i][ord(c) - ord("a")] += 1
        min_count = [0] * 26
        for j in range(26):
            min_count[j] = min([hash_table[i][j] for i in range(len(words))])
        result = []
        for k in range(26):
            if min_count[k] != 0:
                result.extend([chr(ord("a") + k)] * min_count[k])
        return result


# @lc code=end
