# coding: utf-8

class Solution(object):

    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if matrix == [[]] or matrix == []:
            return False

        # 每次都去找右上角那个数字
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if target < matrix[i][j]:  # 如果目标比右上角的数字比小
                j -= 1                 # 把当前列剔除掉
                continue
            if target > matrix[i][j]:  # 如果目标比右上角的数字比大
                i += 1                 # 把当前行剔除掉
        return False

s = Solution()
print s.findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 20)