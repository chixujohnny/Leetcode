# coding: utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True

        stack = []
        s = s.replace(' ','')  # 先去掉空格
        stack.append(s[0])
        for item in s[1:]:
            if item == ')':
                if len(stack) != 0:
                    if stack[-1] == '(': stack.pop(-1)  # 出栈
                    else: return False
                else: return False
            elif item == ']':
                if len(stack) != 0:
                    if stack[-1] == '[': stack.pop(-1)  # 出栈
                    else: return False
                else: return False
            elif item == '}':
                if len(stack) != 0:
                    if stack[-1] == '{': stack.pop(-1)  # 出栈
                    else: return False
                else: return False
            else:  # 否则输入的就是左括号
                stack.append(item)
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid('()]'))