# coding: utf-8

class Solution(object):

    def convert(self, s, numRows):

        if s == "":
            return ""

        if len(s) == 1 or numRows == 1:
            return s

        n = 2*numRows - 2  # 多少个数为一组
        # 需要有多少列
        l = (len(s)/(numRows+numRows-2)) * (numRows-1)
        yu = len(s)%(numRows+numRows-2)
        if yu == 0:
            l = l
        elif yu <= numRows and yu > 0:
            l += 1
        else:
            l += yu-numRows+1

        # 初始化空二维list
        matrix = []
        for a in range(numRows):
            matrix.append([])
            for b in range(l):
                matrix[a].append('')

        # 码字
        x = 0
        y = 0
        down_flag = 1  # 往下码字flag, 为0时向右上码字
        matrix[0][0] = s[0]
        for i in range(1, len(s)):

            # 先走再放
            if down_flag == 1:
                y += 1
                matrix[y][x] = s[i]
                if y == len(matrix)-1:
                    down_flag = 0
                continue

            if down_flag == 0:
                x += 1
                y -= 1
                matrix[y][x] = s[i]
                if y == 0:
                    down_flag = 1

        ret = ''
        for row in matrix:
            for item in row:
                if item != '':
                    ret += item

        return ret


s = Solution()
print(s.convert(s='AB', numRows=1))