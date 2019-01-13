#  coding: utf-8

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #  方法一：创建HashTable  40ms
        l_dict = {}
        for item in nums:
            if l_dict.has_key(item) == False:
                l_dict[item] = 1
            else:
                return True
        return False

        #  方法二：使用set方法  32+ms
        set1 = set(nums)
        if len(set1) != len(nums):
            return False
        else:
            return True