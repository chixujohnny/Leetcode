# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        tag = nums[0]
        i = 1
        ret = 1
        for i in range(i, len(nums)):
            if tag == nums[i]:
                i += 1
            else:
                tag = nums[i]
                ret += 1
                i += 1

        return ret


nums = [1,1,2,2,2,2,3,4,5]
s = Solution()
print( s.removeDuplicates(nums) )