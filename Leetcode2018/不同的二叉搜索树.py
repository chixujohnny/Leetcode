# coding: utf-8

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n+1)
        a[0] = 1
        a[1] = 1
        i = 2
        for i in range(2, n+1):
            for j in range(i):
                a[i] += a[j] * a[i-j-1]
        return a[n]

x = Solution()
print x.numTrees(10)
