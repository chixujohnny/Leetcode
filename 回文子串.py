# coding: utf-8

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        total = 0
        for i in range( len(s)*2-1 ):
            if i%2 == 0:
                total += 1
                l = i/2-1
                r = i/2+1
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    total += 1
                    l -= 1
                    r += 1
            if i%2 == 1:
                l = (i+1)/2-1
                r = (i+1)/2
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    total += 1
                    l -= 1
                    r += 1
        return total

x = Solution()
print x.countSubstrings('aaa')