# coding: utf-8

class Solution(object):

    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        memo = {} # 备忘录

        def dp(K, N):

            # base case
            if K == 1: # 只剩一个鸡蛋
                return N
            if N == 0: # 只剩一个楼层
                return 0

            # 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('inf') # 初始化res，因为我们是要求一个最小值，所以初始化要初始一个无穷大的值
            for i in range(1, N+1):
                # 最坏情况下最少扔鸡蛋的次数
                res = min(
                            #             摔碎了       没摔碎
                            res, max( dp(K-1, i-1), dp(K, N-i) ) +1
                            #    这个max求的是不管在i楼层摔碎还是没摔碎，两种分支取一个尝试次数最多的方案
                      )

            # 存到备忘录
            memo[(K, N)] = res # key是(K,N) value是res
            return res

        return dp(K, N)


s = Solution()
print s.superEggDrop(3, 14)