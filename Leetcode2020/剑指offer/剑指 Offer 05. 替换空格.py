# coding: utf-8

class Solution(object):

    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        while i < len(s):
            if s[i] == ' ':
                s = s[:i] + '%20' + s[i+1:]
                i += 3
                continue
            i += 1

        return s


s = Solution()
print s.replaceSpace("    ")