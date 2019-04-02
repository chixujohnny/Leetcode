# coding: utf-8

class Solution(object):

    def fullJustify(self, words, maxWidth):

        if len(words) == 0:
            return []

        ret = []
        line = []
        i = 0
        while i <= len(words):
            if i == len(words):  # 如果遇到了最后一行，则每个单词中间一个空格，剩下的位置全是空格
                ret.append(' '.join(line) + ' ' * (maxWidth - len(' '.join(line))))
                i += 1
            elif len(line) == 0 and len(words[i]) >= maxWidth:  # 这个单词太长了 或刚好放下
                ret.append(words[i])
                i += 1
                if i == len(words):
                    return ret
                else:
                    continue
            elif len(' '.join(line)) + len(words[i]) + 1 <= maxWidth:  # 贪心，看能不能再装下一个单词
                line.append(words[i])
                i += 1
                continue
            else:  # 装不下了，处理一下这一行line的空格
                # 如果不是最后一行，则每个单词中间的空格要均匀分配，并且左侧的空格多余右侧的空格（这里比较难）
                n = maxWidth - len(''.join(line))  # 剩余空格的个数
                if len(line) == 1:  # 只有一个单词
                    ret.append(line[0] + ' '*n)
                else:
                    j = len(line) - 1  # 需要放空格的位置数
                    dis = []  # 空格的分布
                    while j > 0:
                        dis.append(n/j)
                        n -= n/j
                        j -= 1
                    dis.reverse()
                    j = 0
                    ret_tmp = ''
                    while j < len(line):
                        ret_tmp += line[j]
                        if j != len(line) - 1:
                            ret_tmp = ret_tmp + ' '*dis[j]
                        j += 1
                    ret.append(ret_tmp)
                line = []
        return ret

s = Solution()
print s.fullJustify(['a'],1)
print s.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)