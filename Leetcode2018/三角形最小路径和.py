# coding:utf-8

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)  # 行数,每行的列数=当前行数
        for i in range(m):
            for j in range(i + 1):
                if i == 0 and j == 0:
                    continue
                if i != 0 and j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                if i != 0 and j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                if i != 0 and j != i and j != 0:
                    triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

        for item in triangle:
            print item

        min_item = 0
        for index, item in enumerate( triangle[m-1] ):
            if index == 0:
                min_item = item
            else:
                if item < min_item:
                    min_item = item

        return min_item

x = Solution()
print x.minimumTotal( [[2],[3,4],[6,5,7],[4,1,8,3]] )