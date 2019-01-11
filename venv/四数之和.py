# coding: utf-8

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3:
            return []
        nums_new = sorted(nums)
        result = {}
        for i in range( len(nums) ):
            if i == len(nums) - 3:
                break
            for j in range(i+1, len(nums) ):
                if j == len(nums) - 2:
                    break
                x = j + 1
                y = len(nums) - 1
                while x != y:
                    if nums_new[i] + nums_new[j] + nums_new[x] + nums_new[y] < target:
                        x += 1
                        continue
                    if nums_new[i] + nums_new[j] + nums_new[x] + nums_new[y] > target:
                        y -= 1
                        continue
                    if nums_new[i] + nums_new[j] + nums_new[x] + nums_new[y] == target:
                        key = str(nums_new[i]) + ',' + str(nums_new[j]) + ',' + str(nums_new[x]) + ',' + str(nums_new[y])
                        if result.has_key(key) == False:
                            result[key] = 0
                        x += 1
        result_new = []
        for item in result:
            result_new.append(  map(int, item.split(','))  )
        return result_new

x = Solution()
print x.fourSum([1,0,-1,0,-2,2], 0)