# coding: utf-8

# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         def Combinations(result, s):
#             result_new = []
#             for i in s:  # 'a'
#                 for j in result:
#                     result_new.append(j+i)
#             return result_new
#
#
#         if len(digits) == 0:
#             return []
#         keyboard = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
#         result = []
#         for i, pos in enumerate(digits):
#             if i == 0:
#                 for item in keyboard[int(pos)]:
#                     result.append(item)
#             else:
#                 result = Combinations(result, keyboard[int(pos)])
#         return result
#
# x = Solution()
# print x.letterCombinations('23')  #  output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]



class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == '':
            return []

        dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
                }

        res = []

        digits_list = []   # ['abc','pqrs']
        for item in digits:
            digits_list.append(dict[item])

        def helper(digits_list, path, i):
            if i > len(digits_list):
                return

            if len(path) == len(digits_list):
                res.append(path[:])
                return

            for j in range(len(digits_list[i])):
                path += digits_list[i][j]
                helper(digits_list, path, i+1)
                path = path[:-1]

        helper(digits_list, '', 0)

        return res

s = Solution()
print s.letterCombinations('')
























