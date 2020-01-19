# coding: utf-8

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        queue = []  # BFS的队列

        # 先把周围一圈边界的O打成#
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1):
                    board[i][j] = '#'
                    queue.append((i,j))  # 边界的O打入队列

        # 后面的问题变成了寻找跟#位置联通的O
        # BFS非递归
        while queue != []:  # 只要队列不空就一直循环下去

            # 当前探索点的坐标
            x0 = queue[0][0]
            y0 = queue[0][1]

            # 出队
            queue.pop(0)

            # 在4个方向分别进行探索
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                    board[x][y] = '#'
                    queue.append((x,y)) # 入队

        # 至此已经把所有跟#联通的O标记成了#
        # 下面把剩下的O标记为X，把#标记为O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        for item in board:
            print item

s = Solution()
s.solve([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]])