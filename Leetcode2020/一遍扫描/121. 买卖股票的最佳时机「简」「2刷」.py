# coding: utf-8

# 题解：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        lower = float('inf')
        ret = 0

        for p in prices:
            if p < lower:
                lower = p
            elif p - lower > ret:
                ret = p - lower

        return ret

s = Solution()
print s.maxProfit([7,6,4,3,1])