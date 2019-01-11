# coding: utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 0:
            return False
        if len(x) == 1:
            return True
        if len(x)%2 == 1:  # 字符串长度为奇数
            c = (len(x)-1)/2
            l = c-1
            r = c+1
            while l >=0 and r<len(x):
                if x[l] != x[r]:
                    return False
                else:
                    l -= 1
                    r += 1
                    continue
            return True
        if len(x)%2 == 0:
            l = len(x)/2-1
            r = len(x)/2
            if x[l] != x[r]:
                return False
            while l >=0 and r<len(x):
                if x[l] != x[r]:
                    return False
                else:
                    l -= 1
                    r += 1
                    continue
            return True

x = Solution()
print x.isPalindrome(10101)