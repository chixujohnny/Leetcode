# coding: utf-8

# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

# 输入: "leetcode"
# 输出: "leotcede"

class Solution(object):

    def reverseVowels(self, s):

        # 将每个字符丢进list中
        s_list = []
        for item in s:
            s_list.append(item)

        yuan_dict = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        i = 0
        j = len(s) - 1
        left_flag = 0
        right_flag = 0
        while i <= j:
            if yuan_dict.has_key(s_list[i]) == True:
                left_flag = 1
            else:
                left_flag = 0
                i += 1
            if yuan_dict.has_key(s_list[j]) == True:
                right_flag = 1
            else:
                right_flag = 0
                j -= 1

            if left_flag == 1 and right_flag == 1:
                tag = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = tag
                if j == i+1: break
                else:
                    i += 1
                    j -= 1

        return ''.join(s_list)


s = Solution()
print s.reverseVowels('Aa')
print s.reverseVowels('leetcode')