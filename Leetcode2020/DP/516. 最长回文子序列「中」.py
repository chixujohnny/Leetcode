# coding: utf-8

# 题解: https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E5%AD%90%E5%BA%8F%E5%88%97%E9%97%AE%E9%A2%98%E6%A8%A1%E6%9D%BF.md

class Solution(object):

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 初始化dp-table
        dp = []
        for i in range(len(s)):
            dp.append([0]*len(s))

        # base case
        # dp-table斜对角线置1，表示一个字母对一个字母的最长回文子序列长度为1
        for i in range(len(s)):
            dp[i][i] = 1

        #             dp[i+1][j-1] + 2   if s[i]==s[j]
        # dp[i][j] =
        #             max( dp[i][j-1], dp[i+1][j] )   if s[i]!=s[j]

        for j in range(1, len(s)):
            i = 0
            while j < len(s):

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2

                else:
                    dp[i][j] = max( dp[i][j-1], dp[i+1][j] )

                i += 1
                j += 1

        return dp[0][-1]

s = Solution()
print s.longestPalindromeSubseq('cbbd')