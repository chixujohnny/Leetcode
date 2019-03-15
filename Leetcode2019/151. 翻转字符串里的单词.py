# coding: utf-8

# 给定一个字符串，逐个翻转字符串中的每个单词。

# 输入: "the sky is blue"
# 输出: "blue is sky the"

# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

class Solution(object):

    def reverseWords(self, s):

        if len(s) == 0:
            return ''

        s = s.strip().split(' ')
        i = len(s)-1
        s_new = []
        while i >= 0:
            if s[i] != '':
                s_new.append(s[i])
            i -= 1

        return ' '.join(s_new)

s = Solution()
print s.reverseWords('  hello world!  ')