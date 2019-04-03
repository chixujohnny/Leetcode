# coding: utf-8

# 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"

# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

# 下面的答案有问题，不是最终答案

import copy

class Solution(object):

    def minWindow(self, s, t):

        if len(s) < len(t):
            return ''
        if s == t:
            return s

        T = []
        for item in t:
            T.append(item)

        ret = []
        l = 0
        r = 0
        temp = copy.deepcopy(T)  # 还剩那些T中的字母没被扫到
        d = []     # 目前已经存了那些T中的字母
        l_move_flag = True   # 左指针移动的flag
        r_move_flag = False  # 右指针移动的flag

        while r < len(s) and l < len(s):

            # 移动左指针
            if l_move_flag == True:

                # 先开始扫第一个T中的字母
                if len(temp) == len(t) and len(d) == 0:
                    if s[l] in T:
                        d.append(s[l])
                        l_move_flag = False
                        r_move_flag = True  # 左指针固定，右指针准备往右移动
                        if l < len(s) - 1:
                            r = l + 1
                        else:
                            r = l
                        # 如果t中只有一个字母这种情况
                        if T[0] == d[0] and len(T) == 1:
                            return T[0]
                    else:
                        l += 1

                # 此时的状态应该是刚找到一个substring丢到ret中，并向右移动l寻找能与d[0]元素匹配的字母的位置
                else:
                    if s[l] == d[0]:  # l指针，找到了这个index
                        if set(d) == set(t):  # 如果剩下的依旧匹配T
                            ret.append(s[l:r + 1])
                            l += 1
                            d.pop(0)
                            continue
                        else:
                            l_move_flag = False
                            r_move_flag = True
                            r += 1
                            continue
                    else:  # 没找到这个d[0]，直接l向右移动一个循环找就好
                        l += 1
                        continue


            # 移动右指针
            if r_move_flag == True:

                if s[r] in T:  # 如果右指针的这个字母刚好在T中
                    d.append(s[r])
                    if set(d) == set(T):  # 此时刚好拼出一个子串，就把这个子串丢到ret。此时开始移动左指针
                        ret.append(s[l:r+1])
                        l_move_flag = True
                        r_move_flag = False
                        d.pop(0)  # 把d中第一个元素pop掉
                        l += 1
                    else:  # 如果没有拼出子串，就再向右移动r指针，循环
                        r += 1

                else: # 右指针的这个字母没有在T中，r指针向右移动循环找就好
                    r += 1

        min_substring_len = 9999999
        min_substring = ''
        for item in ret:
            if len(item) < min_substring_len:
                min_substring = item

        return min_substring

s = Solution()
print s.minWindow('ab', 'a')
print s.minWindow('ab', 'b')
print s.minWindow('a', 'b')
print s.minWindow('ADOBECODEBANC', 'ABC')