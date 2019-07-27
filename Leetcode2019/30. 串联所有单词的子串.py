# coding: utf-8

import copy

# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0 or len(words) == 0:
            return []
        if len(s)<len(words[0]):
            return []

        ret = []                  # return list
        len_word = len(words[0])  # length of every word
        words_dict = {}

        # put all words in hash table
        for item in words:
            if words_dict.has_key(item) == False:
                words_dict[item] = 1
            else:
                words_dict[item] += 1

        i = 0
        idx = 0
        idx_flag = True
        words_dict_copy = copy.copy(words_dict)
        while True:
            if len(s) - i < len_word and len(words_dict) != 0:
                break
            if len(words_dict) == 0:
               ret.append(idx)
               idx_flag = False
               words_dict = copy.copy(words_dict_copy)
               i = idx + 1
               continue
            if words_dict.has_key(s[i:i+len_word]) == True:
                if idx_flag == False:
                    idx = i
                    idx_flag = True
                word = s[i:i+len_word]
                words_dict[word] -= 1
                if words_dict[word] == 0:
                    words_dict.pop(word)
                i += len_word
                continue
            if idx_flag == True:
                idx_flag = False
                words_dict = copy.copy(words_dict_copy)
                i = idx
            i += 1

        return ret


s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo","bar"])
