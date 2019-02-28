# coding: utf-8

# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。

# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

# 从后往前遍历数组，如果遇到的元素可以到达最后一行，则截断后边的元素。否则继续往前，若最后剩下的元素大于1个，则可以判断为假。否则就是真，时间复杂度O(n)就可以

class Solution(object):

    def canJump(self, nums):

        if len(nums) == 0:
            return True

        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= len(nums) - i - 1:
                nums = nums[:i+1]
            i -= 1

        if len(nums) == 1:
            return True
        else:
            return False

    def canJump_best_answer(self, nums):

        # 从右边倒数第二个位置往左扫，设置一个计数器n用来记录该位置到尾部还差多少个index
        # 如果该位置元素的值到不了尾部，则计数器+1，表示左边一个元素至少不能小于n+1才能走到尾部
        # 若元素值 >= n 则n归1再往左扫

        len_nums = len(nums)
        if len_nums <= 1:
            return True

        n = 1
        for i in range(len_nums-2, -1, -1):
            if nums[i] < n:
                n += 1
            else:
                n = 1

        if n == 1:
            return True
        else:
            return False


s = Solution()
print s.canJump_best_answer([2,3,1,1,4])
print s.canJump_best_answer([3,2,1,0,4])