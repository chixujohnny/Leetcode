# coding: utf-8

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        if n == 3:
            return 2

        ret = []

        while True:
            if n == 4:
                ret.append(4)
                break
            elif n == 3:
                ret.append(3)
                break
            elif n == 2:
                ret.append(2)
                break
            else:
                ret.append(3)
                n -= 3

        res = 1
        for item in ret:
            res = res * item

        return res

s = Solution()
print s.cuttingRope(2)