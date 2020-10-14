# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0
        dic = {}

        i = -1
        for j in range(len(s)):
            if dic.has_key(s[j]) == True:
                i = dic[s[j]]
            dic[s[j]] = j
            res = max(res, j-i)

        return res


ss = 'abba'

s = Solution()
print s.lengthOfLongestSubstring(ss)