# coding: utf-8

# 此题已收藏，解法比较靠智商

# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

# 输入: [1,2,0]
# 输出: 3

# 说明：你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

# 解：遍历一次数组把大于等于1的和小于数组大小的值放到原数组对应位置，然后再遍历一次数组查当前下标是否和值对应，如果不对应那这个下标就是答案，否则遍历完都没出现那么答案就是数组长度加1。

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        min_num = 1
        while i != len(nums):
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1] and nums[i] != i + 1:
                # 下面这个交换数组中两个元素的写法超绝
                # 要注意必须要把被替换的数写在左边，写反过来不会得到正确的结果
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for item in nums:
            if item == min_num:
                min_num += 1
            else:
                break

        return min_num


s = Solution()
# print s.firstMissingPositive([3,2,5,8,9,6])
# print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])