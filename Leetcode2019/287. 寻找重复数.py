# coding: utf-8

# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

# 输入: [1,3,4,2,2]
# 输出: 2

# 说明
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。

# 此题有点绕，需要复习
# 先用快慢指针思想找到数组中的那个区间内成环
# 然后再在环内找重复的元素

class Solution(object):

    def findDuplicate(self, nums):

        p = q = 0
        while 1:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break
        q = 0
        while p != q:
            p = nums[p]
            q = nums[q]
        return p

s = Solution()
# print s.findDuplicate([1,2,3,3,4])
print s.findDuplicate([3,1,3,4,2])
print s.findDuplicate([1,3,4,2,2])
