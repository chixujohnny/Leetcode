# coding: utf-8

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #  回溯法，此题比较难
        if len(nums) == 1:
            return [nums]
        result = []
        for index in range(len(nums)):
            for item in self.permute(nums[:index] + nums[index+1:]):
                result.append([nums[index]] + item)

        return result

s = Solution()
print(s.permute([1,2,3]))