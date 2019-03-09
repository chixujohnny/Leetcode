# coding: utf-8

# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。

# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

# 这道题使用桶排序，是复杂度O(n)空间复杂度很大，空间换时间的办法

class Solution(object):

    def maximumGap(self, nums):

        if len(nums) < 2:
            return 0

        max_num = max(nums)
        min_num = min(nums)
        bucket = [0] * (max_num - min_num + 1)
        for item in nums:
            bucket[item-min_num] += 1

        sorted_nums = []
        for i, item in enumerate(bucket):
            if item != 0:
                sorted_nums.append(i-min_num)

        max_diff = 0
        for i in range(len(sorted_nums)-1):
            diff = sorted_nums[i+1] - sorted_nums[i]
            if diff > max_diff:
                max_diff = diff

        return max_diff

s = Solution()
print s.maximumGap([3,6,9,1])