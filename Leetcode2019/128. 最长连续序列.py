# coding: utf-8

# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)。

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

# 取出其左右相邻数已有的连续区间长度 left 和 right
# 计算当前数的区间长度为：cur_length = left + right + 1
# 根据 cur_length 更新最大长度 max_length 的值
# 更新区间两端点的长度值

# 此题解法很有意思，适合复习的时候看看

class Solution(object):

    def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0

        max_length = -float('inf')  # 初始化为负无穷
        hash_dict = {}
        for num in nums:
            if hash_dict.has_key(num) == False:
                left = hash_dict.get(num-1, 0)
                right = hash_dict.get(num+1, 0)
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length

                hash_dict[num] = cur_length
                hash_dict[num-left] = cur_length
                hash_dict[num+right] = cur_length

        return max_length

s = Solution()
print s.longestConsecutive([1,2,0,1])
print s.longestConsecutive([100, 4, 200, 1, 3, 2])