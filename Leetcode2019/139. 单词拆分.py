class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [True] + [False] * len(s)

        for start in range(len(s)):
            if dp[start] == True:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        dp[end] = True

        return dp[-1]


s = Solution()
s.wordBreak("leetcode", ["leet","code"])