# coding: utf-8

# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         dp = [0] * (target+1)
#
#         dp[0] = 1
#
#         for i in range(1, target+1):
#             for j in range(len(nums)):
#                 if i >= nums[j]:
#                     dp[i] += dp[i - nums[j]]
#
#         return dp[-1]
#
# s = Solution()
# print s.combinationSum4([4,2,1], 32)



# 回溯+备忘录法题解：https://leetcode-cn.com/problems/combination-sum-iv/solution/dfszi-dian-bao-cun-by-iversonlaotang/

class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        memo = {}

        def helper(nums, target):
            if target == 0:
                return 1

            if target in memo:
                return memo[target]

            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += helper(nums, target-nums[i])

            memo[target] = res
            return res

        return helper(nums, target)

s = Solution()
print s.combinationSum4([4,2,1], 32)

































