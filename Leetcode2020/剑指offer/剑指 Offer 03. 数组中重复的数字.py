# coding: utf-8

class Solution(object):

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = {}

        for item in nums:
            if d.has_key(item) == False:
                d[item] = 1
            else:
                return item

s = Solution()
print s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])