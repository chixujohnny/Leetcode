# coding: utf-8

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def helper(nums, path):

            if path not in nums:
                res.append(path[:])

            for i in range(len(nums)):
                helper(nums.pop(i), path.append(nums[i]))

        helper(nums, [])

        return res


s = Solution()
s.permuteUnique([1,1,2])