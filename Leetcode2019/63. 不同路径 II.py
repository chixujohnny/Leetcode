class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        dp = obstacleGrid
        row_stop_flag = False
        col_stop_flag = False

        if dp[0][0] == 1:
            return 0

        if n == 1:  # 只有一行
            if 1 in dp[0]:
                return 0
            else:
                return 1

        if m == 1:  # 只有一列
            for item in dp:
                if item == [1]:
                    return 0
            return 1

        for i in range(n):
            for j in range(m):
                if i == 0:
                    if dp[i][j] == 1:
                        dp[i][j] = -1
                        row_stop_flag = True
                    else:
                        if row_stop_flag == True:
                            dp[i][j] = -1
                        else:
                            dp[i][j] = 1

                elif j == 0:
                    if dp[i][j] == 1:
                        dp[i][j] = -1
                        col_stop_flag = True
                    else:
                        if col_stop_flag == True:
                            dp[i][j] = -1
                        else:
                            dp[i][j] = 1

                else:
                    if dp[i][j] == 1:
                        dp[i][j] = -1

        for i in range(1, n):
            for j in range(1, m):
                if dp[i][j] != -1:
                    if dp[i - 1][j] != -1 and dp[i][j - 1] != -1:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif dp[i - 1][j] == -1 and dp[i][j - 1] != -1:
                        dp[i][j] = dp[i][j - 1]
                    elif dp[i - 1][j] != -1 and dp[i][j - 1] == -1:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = -1

        if dp[-1][-1] == -1:
            return 0
        else:
            return dp[-1][-1]