# coding: utf-8

# Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]
#
# Output: 2
#
# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]


def function(grid):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    zombielist = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                zombielist.append([i,j])  # 将zombie的坐标拍如队列

    minute = 0
    while zombielist != []:
        newzombielist = []
        for zombienode in zombielist:
            x0 = zombienode[0]
            y0 = zombienode[1]

            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                    grid[x][y] = 1
                    newzombielist.append([x,y])

            if newzombielist == []:
                break

        zombielist = newzombielist[:]
        minute += 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid == 0:  # 还有没被感染的人
                return -1

    return minute

print function([[0, 1, 1, 0, 1],[0, 1, 0, 1, 0],[0, 0, 0, 0, 1],[0, 1, 0, 0, 0]])
