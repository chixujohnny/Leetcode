# coding: utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 分两种情况
        dp = [0] * len(nums)
        dpdp = [0] * len(nums)

        # 打劫第一家但不打劫最后一家
        dp[1] = nums[0]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        # 打劫最后一家，但不打劫第一家
        dpdp[1] = nums[1]
        for i in range(2, len(nums)):
            dpdp[i] = max(dpdp[i - 1], dpdp[i - 2] + nums[1:][i - 1])

        return max(dp[-1], dpdp[-1])


s = Solution()
# s.rob([2,3,2])
print s.rob([1,2,3,1])