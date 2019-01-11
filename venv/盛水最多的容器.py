# coding: utf-8

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_water = 0
        while i != j:
            water = (j-i) * min(height[i], height[j])
            if water > max_water:
                max_water = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water

x = Solution()
print x.maxArea([1,8,6,2,5,4,8,3,7])