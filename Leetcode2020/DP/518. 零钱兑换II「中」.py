# coding: utf-8

# 题解：https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0] * (amount + 1)
        dp[0] = 1  # base case

        for coin in coins:
            for i in range(coin, amount+1):  # 循环左边界从coin开始, 因为小于coin的部分看了没有意义
                dp[i] = dp[i] + dp[i-coin]

        return dp[-1]


s = Solution()
print s.change(5, [1,2,5])