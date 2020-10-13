# coding: utf-8

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == [[]]:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i][j-1], grid[i-1][j])

        return grid[-1][-1]
