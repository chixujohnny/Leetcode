# coding: utf-8

# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int1
#         :rtype: List[str]
#         """
#
#         #  回溯法
#         ans = []
#         def backtrack(S = '', left = 0, right = 0):
#             if len(S) == 2 * n:  # 递归结束的条件
#                 ans.append(S)
#                 return
#             if left < n:  # 如果左括号数量少于n，则可以添加一个左括号
#                 backtrack(S+'(', left+1, right)
#             if right < left:  # 如果左括号比右括号多的话
#                 backtrack(S+')', left, right+1)
#
#         backtrack()
#         return ans
#
# s = Solution()
# print(s.generateParenthesis(n=3))



class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n <= 0:
            return [""]

        def isTrue(path):  # 判断这个字符串是否符合标准
            stack_num = 0
            for item in path:
                if item == '(':
                    stack_num += 1
                else:
                    stack_num -= 1
                if stack_num < 0:
                    return False
            return True

        res = []

        def helper(path, left_remain_num, right_remain_num):
            if left_remain_num == 0 and right_remain_num == 0 and isTrue(path) == True:
                res.append(path)

            # 添加'('
            if left_remain_num > 0:
                path += '('
                helper(path, left_remain_num-1, right_remain_num)
                path = path[:-1]
            # 添加')'
            if right_remain_num > 0:
                path += ')'
                helper(path, left_remain_num, right_remain_num-1)
                path = path[:-1]

        helper('(', n-1, n)

        return res

s = Solution()
print s.generateParenthesis(3)



























