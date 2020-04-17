# coding: utf-8

# 解法链接：https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/

# str1 = 'abcde'
# str2 = 'ace'
# output = 3


class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m, n = len(text1), len(text2)

        dp = [ [0]*(n+1) for _ in range(m+1) ]
        for i in range( len(text1) + 1 ):
            for j in range( len(text2) + 1 ):
                dp[i][j] = 0

        # dp[0][x] 和 dp[y][0] 这两个边界位置表示null，dp[0][0] = 0，多做这个边界的目的是防止数组越界

        # 状态转移方程:
        #
        #              dp[i][j] + 1                      (if text1[i-1] == text2[j-1])
        # dp[i][j] =
        #              max(dp[i-1][j], dp[i][j-1])       (if text1[i-1] == text2[j-1])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1

                elif text1[i-1] != text2[j-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


s = Solution()
print s.longestCommonSubsequence('abcde','ace')