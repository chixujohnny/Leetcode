class Solution(object):
    def ordinalOfDate(self, date):
        """
        :type date: str
        :rtype: int
        """

        y = int(date.split('-')[0])
        m = int(date.split('-')[1])
        d = int(date.split('-')[2])

        d_all = [31,28,31,30,31,30,31,31,30,31,30,31]
        res = 0

        for i in range(1, m):
            res += d_all[i-1]
            if i == 2 and y == 2000:
                res += 1
            elif i == 2 and y%4 == 0 and y!=1900:
                res += 1

        res += d

        return res

s = Solution()
print s.ordinalOfDate("2004-03-01")