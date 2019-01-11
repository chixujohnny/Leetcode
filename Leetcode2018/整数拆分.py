# coding: utf-8

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        elif n == 1: return 0
        elif n == 2: return 1
        elif n == 3: return 3
        elif n == 4: return 4
        else:
            total = 1
            l = 0
            while True:
                l = n - 3
                if l == 0:
                    return total * 3
                if l == 2:
                    return total * 3 * 2
                if l == 4:
                    return total * 3 * 4
                total = total * 3
                n -= 3


x = Solution()
print x.integerBreak(10)