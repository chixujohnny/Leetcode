# coding: utf-8

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # 备忘录
        memo = {}

        def dp(n):

            # 查备忘录避免重复计算
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1

            res = float('INF')  # 正无穷

            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res  = min(res, 1 + subproblem)

            # 记入备忘录
            if res != float('INF'):
                memo[n] = res
            else:
                memo[n] = -1

        return dp(amount)