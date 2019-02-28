# coding: utf-8

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

# 输入: [7,1,5,3,6,4]
# 输出: 7

# 贪心算法：只要第二天比该天价格高，该天就买进，第二天卖出，往复循环。时间复杂度O(n)

class Solution(object):

    def maxProfit(self, prices):

        if len(prices) <= 1:
            return 0

        ret = 0
        for i in range(len(prices) -1):
            if prices[i] < prices[i+1]:
                ret = ret + prices[i+1] - prices[i]

        return ret


s = Solution()
print s.maxProfit([7,1,5,3,6,4])