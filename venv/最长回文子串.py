# coding: utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_string = ''
        for i in range( len(s)*2-1 ):
            if i%2 == 0:
                if len(max_string) == 0:
                    max_string = s[i/2]
                l = i/2-1
                r = i/2+1
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    if len( s[l:r+1] ) > len(max_string):
                        max_string = s[l:r+1]
                    l -= 1
                    r += 1
            if i%2 == 1:
                l = (i+1)/2-1
                r = (i+1)/2
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    if len( s[l:r+1] ) > len(max_string):
                        max_string = s[l:r+1]
                    l -= 1
                    r += 1

        return max_string

x = Solution()
print x.longestPalindrome('ccc')