# coding: utf-8

import collections

# Amazon OA题

# BFS

# 思路：每一轮，腐烂将会从每一个烂橘子蔓延到与其相邻的新鲜橘子上。一开始，腐烂的橘子的深度为 0，每一轮腐烂会从腐烂橘子传染到之相邻新鲜橘子上，并且设置这些新的腐烂橘子的深度为自己深度 +1，我们想知道完成这个过程之后的最大深度值是多少。

# 算法：我们可以用一个广度优先搜索来建模这一过程。因为我们总是选择去使用深度值最小的（且之前未使用过的）腐烂橘子去腐化新鲜橘子，如此保证每一个橘子腐烂时的深度标号也是最小的。
#       我们还应该检查最终状态下，是否还有新鲜橘子。


class Solution(object):

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # dx,dy表示BFS时可以走的四个方向
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        rotlist = []  # 烂橘子队列
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:  # 把所有烂橘子坐标拍到队列里
                    rotlist.append([i,j])

        minute = 0
        while(rotlist):  # BFS循环
            newrotlist = []
            for rotnode in rotlist:
                x0 = rotnode[0]  # 烂橘子x轴位置
                y0 = rotnode[1]  # 烂橘子y轴位置

                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]

                    # 如果在上下左右任意四个方向行走一步之后能遇到好橘子
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        newrotlist.append([x,y])  # 把新的烂橘子坐标拍到队列中

            if newrotlist == []:
                break  # 没有可以遍历的烂橘子就可以退出while了

            rotlist = newrotlist[:]
            minute += 1

        for row in grid:
            for i in row:
                if i == 1:  # 还有新鲜的
                    return -1

        return minute

s = Solution()
print s.orangesRotting([[0,2]])