# coding: utf-8

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def helper(nums, path):

            if nums == []:
                res.append(path[:])
                return

            for i in range(len(nums)):
                path.append(nums[i])
                helper(nums[:i] + nums[i + 1:], path)
                path.pop()

        helper(nums, [])

        return res

s = Solution()
print(s.permute([1,2,3]))