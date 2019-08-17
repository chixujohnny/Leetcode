# coding: utf-8

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):  # i表示当前的目标金额
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1]


s = Solution()
print s.coinChange([1,2,5], 11)