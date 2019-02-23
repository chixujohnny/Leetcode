# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        left_tag = nums[0]
        right_tag = nums[1]
        i = 2

        while i < len(nums):
            if nums[i] == left_tag and nums[i] == right_tag:
                nums.pop(i)
                continue
            if nums[i] != left_tag and nums[i] == right_tag:
                left_tag = right_tag
                right_tag = nums[i]
                i += 1
                continue
            if nums[i] == left_tag and nums != right_tag:  # right_tag == None
                right_tag = nums[i]
                i += 1
                continue
            if nums[i] != left_tag and nums[i] != right_tag:
                left_tag = nums[i]
                right_tag = None
                i += 1

        return len(nums)

s = Solution()
print s.removeDuplicates([1,1,1,2,2,3])
print s.removeDuplicates([0,0,1,1,1,1,2,3,3])
print s.removeDuplicates([1])
print s.removeDuplicates([1,2])
print s.removeDuplicates([])
print s.removeDuplicates([1,1,1,1,1,1])