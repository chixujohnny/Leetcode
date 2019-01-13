# coding: utf-8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int1
        :rtype: List[str]
        """

        #  回溯法
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:  # 递归结束的条件
                ans.append(S)
                return
            if left < n:  # 如果左括号数量少于n，则可以添加一个左括号
                backtrack(S+'(', left+1, right)
            if right < left:  # 如果左括号比右括号多的话
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

s = Solution()
print(s.generateParenthesis(n=3))
