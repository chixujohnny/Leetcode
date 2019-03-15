# coding: utf-8

# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

class Solution(object):

    def canConstruct(self, ransomNote, magazine):

        if len(magazine) < len(ransomNote):
            return False
        if len(ransomNote) == 0:
            return True

        rans_dict = {}
        for item in ransomNote:
            if rans_dict.has_key(item) == False:
                rans_dict[item] = 1
            else:
                rans_dict[item] += 1

        for item in magazine:
            if rans_dict.has_key(item)== True:
                rans_dict[item] -= 1
                if rans_dict[item] == 0:
                    rans_dict.pop(item)
            if len(rans_dict) == 0:
                return True
        return False

s = Solution()
print s.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
print s.canConstruct('','')
print s.canConstruct('','a')
print s.canConstruct('a','b')
print s.canConstruct('aa','ab')
print s.canConstruct('aa','aab')
