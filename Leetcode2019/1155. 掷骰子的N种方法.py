class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        dp = [0] * (target+1)
        dp[0] = 1

        for i in range(1, len(dp)):

            for j in range(1, f+1):

                for k in range(d):

                    if i >= j:
                        dp[i] += dp[i-j]

        return dp[-1]

s = Solution()
s.numRollsToTarget(1,6,3)