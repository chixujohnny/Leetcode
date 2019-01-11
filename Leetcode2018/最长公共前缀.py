# coding: utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        pre_str = ''
        for i in range(len(strs[0])):
            try:
                if strs[0][i] == strs[1][i]:
                    pre_str += strs[0][i]
                else:
                    break
            except:
                break
        if pre_str == '':
            return ''
        for i in range(2, len(strs)):
            if pre_str == strs[i][:len(pre_str)]:
                continue
            else:
                j = len(pre_str) - 1
                while j >= 0:
                    try:
                        if pre_str[j] != strs[i][j]:
                            pre_str = pre_str[:-1]
                            j -= 1
                        else:
                            break
                    except:
                        pre_str = pre_str[:-1]
                        j -= 1
        return pre_str

x = Solution()
print x.longestCommonPrefix(["c","c"])