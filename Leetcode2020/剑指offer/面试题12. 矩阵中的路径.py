# coding: utf-8

import copy

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, k, visited):
            # 递归结束的条件
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or board[i][j] != word[k] or visited[i][j]==1:
                return False
            if k == len(word)-1:
                return True
            visited[i][j] = 1
            return dfs(i+1,j,k+1,visited) or dfs(i-1,j,k+1,visited) or dfs(i,j+1,k+1,visited) or dfs(i,j-1,k+1,visited)

        a = []
        for i in range(len(board[0])):
            a.append(0)
        visited = []
        for i in range(len(board)):
            visited.append(copy.deepcopy(a))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, visited) == True:
                    return True

        return False

s = Solution()
print s.exist([["a","b"],["c","d"]], "abcd")
print s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
print s.exist([['a','a']], 'aa')
print s.exist([['a','b']], 'ba')
print s.exist([['a']], 'ab')
print s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], 'AAB')