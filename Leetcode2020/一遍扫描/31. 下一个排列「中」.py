# coding: utf-8

# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# 此题经典，考验智商题，适合复习
# 这个道题Leetcode没通过，不知道咋回事，代码完全一样的  用例[1,3,2]

class Solution(object):

    def reverse(self, nums, l):
        return nums[:l+1] + list(reversed(nums[l+1:]))

    def swap(self, nums, l, r):
        tag = nums[l]
        nums[l] = nums[r]
        nums[r] = tag
        return nums

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        else:
            l = len(nums) - 1
            tag = -99999
            ret_flag = False
            while True:
                if ret_flag == True:
                    break
                if l < 0:
                    nums = self.reverse(nums, l)  # reverse right part of nums
                    break
                elif nums[l] >= tag:
                    tag = nums[l]
                    l -= 1
                else:
                    r = l + 1
                    flag =  nums[l]
                    while True:
                        # finding number just larger than nums[l]
                        if r >= len(nums):
                            nums = self.swap(nums, l, r-1)
                            nums = self.reverse(nums, l)
                            ret_flag = True
                            break
                        elif nums[r] > nums[l]:
                            flag = nums[r]
                            r += 1
                        elif nums[r] < flag:
                            r -= 1
                            nums = self.swap(nums, l, r)
                            nums = self.reverse(nums, l)
                            ret_flag = True
                            break

            return nums

s = Solution()
print (s.nextPermutation([1,3,2]))
print (s.nextPermutation([1,1]))
print (s.nextPermutation([3,2,1]))
print (s.nextPermutation([1,5,8,4,7,6,5,3,1]))
print (s.nextPermutation([1,2,3]))
print (s.nextPermutation([1,1,5]))
print (s.nextPermutation([5,1,5]))
print (s.nextPermutation([1]))



class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0 or len(nums) == 1:
            return nums

        def swap():
            return

        def reverse():
            return

        # step1:从后往前找第一对相邻升序的index
        tag_index = -1
        for i in range(len(nums), 1, -1):
            if nums[i-1] < nums[i]:
                tag_index = i-1
                break

        if tag_index == -1:
            return reverse(nums)
        else:
            # 寻找在 tag_index+1 右侧比nums[tag_index]大的最小的一个index
            min_num = float('inf')
            # for i in range(len(nums), tag_index):





























