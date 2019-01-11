# coding:utf-8

# 有一个数字出现一次，剩下的数字出现3次

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0] * 32
        for i in nums:
            if i < 0:
                temp[0] += 1
                i = abs(i)
            b = bin(i)
            for index, item in enumerate(str(b[2:])):
                if item == '1':
                    temp[ 32 - len(str(b[2:])) + index ] += 1

        r = ''
        for item in temp:
            if item % 3 != 0:
                r += '1'
            else:
                r += '0'
        if r[0] == '1':
            return -int(r[1:], 2)
        else:
            return int(r, 2)


# x = Solution()
# print x.singleNumber([-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555])
