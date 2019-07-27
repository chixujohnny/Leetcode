# coding: utf-8

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

# 说明：
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。

# 好题，不过有点考智商
# 先把前len(nums)-k部分reverse，再对后面reverse，最后做一遍reverse，时间复杂度O(n)
# 或者挪动k次，时间复杂度O(kn)

class Solution(object):
    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        self.reverse(nums, 0, l - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, l - 1)

s = Solution()
print s.rotate([1,2,3,4,5,6], k=4)
print s.rotate([1,2,3,4,5,6,7,8], k=2)
print s.rotate([1,2,3,4,5,6,7,8,9], k=3)
print s.rotate([1,2,3,4,5,6], k=2)
print s.rotate([1,2], k=3)
print s.rotate([1,2,3,4,5,6,7,8], k=3)
print s.rotate([1,2,3,4,5,6,7], k=3)