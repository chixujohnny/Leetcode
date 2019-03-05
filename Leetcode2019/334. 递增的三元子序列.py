# coding: utf-8

# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。

# 输入: [1,2,3,4,5]
# 输出: true

# 输入: [5,4,3,2,1]
# 输出: false

# 贪心思想，从左向右找最小值和次小值，当某个数大于最小值和次小值的时候return True
# 题不难，但是思路挺有意思的，可以好好看看

class Solution(object):

    def increasingTriplet(self, nums):

        if len(nums) < 3:
            return False

        nums1 = 2147483647
        nums2 = 2147483647
        for item in nums:
            if item <= nums1:
                nums1 = item
            elif item > nums1 and item <= nums2:
                nums2 = item
            else:  # item > nums1 and item > nums2
                return True
        return False


s = Solution()
print s.increasingTriplet([1,0,2,0,-1,-1,3])
print s.increasingTriplet([1,2,-10,-8,-7])
print s.increasingTriplet([1,1,1,1,1,1,1,1])
print s.increasingTriplet([5,1,5,5,2,5,4])
print s.increasingTriplet([5,4,3,2,1])
print s.increasingTriplet([2,1,5,0,3])