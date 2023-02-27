#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = collections.Counter(ransomNote)
        dict_magazine = collections.Counter(magazine)
        dict_diff = dict_ransomNote - dict_magazine
        print(dict_diff)
        if len(dict_diff) > 0:
            return False
        return True
        # def string_to_array(string):
        #     array = [0] * 26
        #     for c in string:
        #         array[ord(c) - ord("a")] += 1
        #     return array

        # ransomNote_array = string_to_array(ransomNote)
        # magazine_array = string_to_array(magazine)
        # for i in range(26):
        #     # 如果有字符在 ransomNote_array 中的数量比在 magazine_array 中的数量多，则说明 ransomNote 能不能由 magazine 里面的字符构成
        #     if ransomNote_array[i] - magazine_array[i] > 0:
        #         return False
        # return True


# @lc code=end
