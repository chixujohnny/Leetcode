# coding: utf-8

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0]+nums[1]
        closest = 99999
        closest_s = 0
        sums_sorted = sorted(nums)
        for index, item in enumerate(sums_sorted):
            if index == len(sums_sorted) - 2:
                break
            i = index + 1
            j = len(sums_sorted) - 1
            while i != j:
                s = item + sums_sorted[i] + sums_sorted[j]
                if s < target:
                    if abs(s - target) < closest:
                        closest = abs(s - target)
                        closest_s = s
                    i += 1
                if s > target:
                    if abs(s - target) < closest:
                        closest = abs(s - target)
                        closest_s = s
                    j -= 1
                if s == target:
                    return target
        return closest_s

x = Solution()
print x.threeSumClosest([1,1,1,0], -100)
print x.threeSumClosest([1,1,1,1], 0)
print x.threeSumClosest([0,5,-1,-2,4,-1,0,-3,4,-5], 1)