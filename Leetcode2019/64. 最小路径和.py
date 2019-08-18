# coding: utf-8

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 初始化dp
        # dp = [[-1] * len(grid[0])] * len(grid)
        dp = []
        for i in range(len(grid)):
            dp.append([-1]*len(grid[0]))
        dp[0][0] = grid[0][0]

        # 初始化第一行和第一列
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                if j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j-1])

        return dp[-1][-1]

s = Solution()
print s.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])