# coding: utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        max_len = 1
        i=0
        while i < len(s):
            d = {}
            j = i
            cf = False
            while j < len(s):
                if d.has_key(s[j]) == False:
                    d[s[j]] = j
                    j += 1
                else: # 出现了重复的字符
                    cf = True
                    i = d[s[j]] + 1
                    break
            if len(d) > max_len:
                max_len = len(d)
            if cf != True:
                i += 1

        return max_len

x = Solution()
print x.lengthOfLongestSubstring('aab')
print x.lengthOfLongestSubstring('dvdf')