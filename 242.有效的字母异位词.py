#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array_s = [0] * 26
        for c in s:
            array_s[ord(c) - ord("a")] += 1
        array_t = [0] * 26
        for c in t:
            array_t[ord(c) - ord("a")] += 1
        for i in range(26):
            if array_s[i] != array_t[i]:
                return False
        return True


# @lc code=end
