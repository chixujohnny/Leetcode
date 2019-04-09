# coding: utf-8

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

# 这道题比较拼智商，要背一下

class Solution(object):

    def maxSubArray(self, nums):

        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])