# coding: utf-8

class Solution(object):

    def findLongestSubstring(self, final):
        final = sorted(final)
        ret = 1
        ret_list = []
        for i, item in enumerate(final):
            if i+1 < len(final):
                if final[i+1] - item == 1:
                    ret += 1
                else:
                    ret_list.append(ret)
                    ret = 1
            else:
                ret_list.append(ret)

        if ret_list == []:
            if ret != 1:
                return ret
            else:
                return 0
        else:
            return max(ret_list)

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return 0

        stack = []  # storage index of "(" in a stack
        final = []  # storage all index of "("&")" in a list

        for i, item in enumerate(s):
            if item == ')':
                if stack != []:
                    final.append(stack[-1])
                    final.append(i)
                    stack.pop()
                    continue
                else:  # stack == []
                    continue
            if item == '(':
                stack.append(i)

        return self.findLongestSubstring(final)


s = Solution()
print s.longestValidParentheses('(()')
print s.longestValidParentheses(')(())(()()()(((')
print s.longestValidParentheses('()(()')
print s.longestValidParentheses('(()')
print s.longestValidParentheses('(())()')
print s.longestValidParentheses(')(())')
print s.longestValidParentheses(')()()(')
print s.longestValidParentheses('')
print s.longestValidParentheses('(')
print s.longestValidParentheses(')(')