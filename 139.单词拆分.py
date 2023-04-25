#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # 计算字符串长度
        s_length = len(s)
        # 初始化 dp 数组
        dp = [0 for _ in range(s_length + 1)]
        dp[0] = 1
        # 遍历背包容量
        for j in range(1, s_length + 1):
            # 遍历物品
            for word in wordDict:
                word_length = len(word)
                # 如果当前 word 长度超过 j，则一定无法由 word 拼接出前 j 个字符，可以跳过
                if word_length > j:
                    continue
                else:
                    # 如果 dp[j-word_length] 可以拼接，并且从第 j - word_length 个字符到第 j 个字符刚好等于 word，则说明dp[j] 也可以拼接
                    if dp[j - word_length] == 1 and s[j - word_length : j] == word:
                        dp[j] = 1
        if dp[-1]:
            return True
        else:
            return False


solution = Solution()
solution.wordBreak("leetcode", ["leet", "code"])

# @lc code=end
