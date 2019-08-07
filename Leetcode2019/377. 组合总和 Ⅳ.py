class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        dp = [0] * (target+1)

        dp[0] = 1

        for i in range(1, target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]

s = Solution()
print s.combinationSum4([4,2,1], 32)