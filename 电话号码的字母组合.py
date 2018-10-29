# coding: utf-8

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def Combinations(result, s):
            result_new = []
            for i in s:  # 'a'
                for j in result:
                    result_new.append(j+i)
            return result_new


        if len(digits) == 0:
            return []
        keyboard = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result = []
        for i, pos in enumerate(digits):
            if i == 0:
                for item in keyboard[int(pos)]:
                    result.append(item)
            else:
                result = Combinations(result, keyboard[int(pos)])
        return result

x = Solution()
print x.letterCombinations('23')  #  output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]