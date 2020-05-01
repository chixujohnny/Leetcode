# coding: utf-8

class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if word == '':
            return False

        self.res = False

        for y in range(len(board)):
            for x in range(len(board[0])):

                path = board[y][x]
                path_index = [[x,y]]

                def helper(board, word, path, path_index, y, x):

                    if word[:len(path)] != path:  # 如果路线走歪了就不用再往下走了
                        return

                    if word == path:
                        self.res = True
                        return

                    # 先走再append
                    # 向右走
                    if x < len(board[0])-1 and [x+1, y] not in path_index:
                        x += 1
                        path += board[y][x]
                        path_index.append([x,y])
                        helper(board, word, path, path_index, y, x)
                        path = path[:-1]
                        x -= 1
                        path_index.pop()
                        if self.res == True:
                            return

                    # 向下走
                    if y < len(board)-1 and [x, y+1] not in path_index:
                        y += 1
                        path += board[y][x]
                        path_index.append([x, y])
                        helper(board, word, path, path_index, y, x)
                        path = path[:-1]
                        y -= 1
                        path_index.pop()
                        if self.res == True:
                            return

                    # 向左走
                    if x > 0 and [x-1, y] not in path_index:
                        x -= 1
                        path += board[y][x]
                        path_index.append([x, y])
                        helper(board, word, path, path_index, y, x)
                        path = path[:-1]
                        x += 1
                        path_index.pop()
                        if self.res == True:
                            return

                    # 向上走
                    if y > 0 and [x, y-1] not in path_index:
                        y -= 1
                        path += board[y][x]
                        path_index.append([x, y])
                        helper(board, word, path, path_index, y, x)
                        path = path[:-1]
                        y += 1
                        path_index.pop()
                        if self.res == True:
                            return

                helper(board, word, path, path_index, y, x)

        return self.res

s = Solution()
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED")
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "SEE")
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB")
print s.exist([["a","b"],["c","d"]], "cabd")
print s.exist([["a","b"],["c","d"]], "acbd")
print s.exist([["a","b"],["c","d"]], "acdb")
print s.exist([["a","b"],["c","d"]], "dbac")
print s.exist([["A","B","C"],["H","G","D"],["I","F","E"]], "ABCDEFGHI")