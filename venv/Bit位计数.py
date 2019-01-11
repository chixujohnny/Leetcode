# coding:utf-8

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 1:
            return [0, 1]
        rec = [0, 1]
        while len(rec) <= num:
            temp = [x + 1 for x in rec]
            rec = rec + temp
        return rec[:num+1]

x = Solution()
print( x.countBits(2) )