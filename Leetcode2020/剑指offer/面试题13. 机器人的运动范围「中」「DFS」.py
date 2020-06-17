# coding: utf-8

import copy

class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        # 计算每个位数之和
        def countSum(x, y):
            total=0
            concat = str(x) + str(y)
            for item in concat:
                total += int(item)
            return total

        def helper(m, n, k, i, j, visited):
            # 定义递归出口
            if i<0 or j<0 or i>=m or j>=n or countSum(i,j)>k or visited[i][j]==1:
                return 0
            visited[i][j] = 1
            return 1 + helper(m,n,k,i+1,j,visited) + helper(m,n,k,i-1,j,visited) + helper(m,n,k,i,j+1,visited) + helper(m,n,k,i,j-1,visited)

        row = []
        for i in range(n):
            row.append(0)
        visited = []
        for i in range(m):
            visited.append(copy.deepcopy(row))

        return helper(m, n, k, 0, 0, visited)


s = Solution()
print s.movingCount(2,3,1)
print s.movingCount(3,1,0)
print s.movingCount(3,2,17)