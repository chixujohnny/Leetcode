# coding: utf-8

# 题解：https://github.com/labuladong/fucking-algorithm/blob/master/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%B3%BB%E5%88%97/%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.md

# 这道题太难了

class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # 初始化dp-table
        dp = []
        for i in range(len(word1)+1):
            dp.append([0]*(len(word2)+1))

        for i in range(len(word2)+1):
            dp[0][i] = i
        for j in range(len(word1)+1):
            dp[j][0] = j

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[-1][-1]


s = Solution()
print s.minDistance('rad','apple')
print s.minDistance('horse','ros')
print s.minDistance('intention','execution')