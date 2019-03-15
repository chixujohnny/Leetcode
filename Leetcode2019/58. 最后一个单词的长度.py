# coding: utf-8

class Solution(object):

    def lengthOfLastWord(self, s):

        if len(s.replace(' ','')) == 0:
            return 0

        s = s.strip().split(' ')
        return len(s[-1])

s = Solution()
print s.lengthOfLastWord(' ')
print s.lengthOfLastWord('hello world')