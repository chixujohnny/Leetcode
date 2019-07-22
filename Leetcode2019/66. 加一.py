# coding: utf-8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        zero_num = 0  # 记录有多少进位置0的

        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
                else:
                    i -= 1

s = Solution()
print s.plusOne([9,9,9,9,9])
print s.plusOne([1,2,3])
print s.plusOne([1,3,4,9,9,9])