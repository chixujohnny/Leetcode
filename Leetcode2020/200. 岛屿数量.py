# coding: utf-8

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        islandNum = 0
        islandList = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    islandList.append([i,j])  # 待探索陆地坐标排入队列
                    grid[i][j] = '0'

                    while islandList != []:  # 开始BFS

                        # 当前探索点坐标
                        x0 = islandList[0][0]
                        y0 = islandList[0][1]

                        for k in range(4):  # 待探索陆地在四个方向进行探索
                            x = x0 + dx[k]
                            y = y0 + dy[k]
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                                grid[x][y] = '0'  # BFS探索到的陆地变成水
                                islandList.append([x,y])  # BFS探索到的陆地坐标拍入队列

                        islandList.pop(0)

                    islandNum += 1  # 每BFS一轮即找到一个岛屿

        return islandNum

s = Solution()
print s.numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])
print s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])