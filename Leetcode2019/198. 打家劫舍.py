class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums)+1)

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i-1])

        return dp[-1]


s = Solution()
print s.rob([2,1,1,2])