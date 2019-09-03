# coding: utf-8

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 厄拉多塞筛法

        if n in [0,1]:
            return 0

        nums = [1] * n
        nums[0] = nums[1] = 0

        res = 0
        for i in range(2, int(n**0.5)+1):
            if nums[i] == 1:
                tmp = [0] * len(nums[i*i : n : i])
                nums[i*i : n : i] = tmp


        return sum(nums)


s = Solution()
print s.countPrimes(1)