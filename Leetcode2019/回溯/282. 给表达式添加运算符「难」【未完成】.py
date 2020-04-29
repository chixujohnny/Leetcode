# coding: utf-8

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        # -----------------  UDF  ----------------- #
        def isNum(item):  # 判断这个字符串是否能转为一个int型数字
            if item[0] == '0' and len(item)>1:
                return False
            else:
                return True

        def caculate(path): # 输入包含['+','-','*']运算的式子，输出运算结果
            # 把path中第一个运算符去掉
            path = path[1:]

            # 扫第一遍，确定所有'*'的index
            mul_index = []
            for i, item in enumerate(path):
                if item == '*':
                    mul_index.append(i)

            # 扫第二遍，把乘法式子捞出来单独计算掉
            for index in mul_index:

                # 找这个乘号左边的数
                left_num = ''
                l = index - 1
                while l>=0 and path[l] != '+' and path[l] != '-':
                    left_num = path[l] + left_num
                    l -= 1
                left_num = int(left_num)
                l += 1

                # 找乘号右边那个数
                right_num = ''
                r = index + 1
                while r<len(path) and path[r] != '+' and path[r] != '-':
                    right_num = right_num + path[r]
                    r += 1
                right_num = int(right_num)
                r += 1

                # 乘积
                mul = str(left_num*right_num)

                # 替换
                path[l:r+1] = ' '*(r+1-l)
                for i, item in enumerate(mul):
                    path[l+i] = item

            # 清除空格
            path = path.replace(' ','')

            # 计算加减法部分
            total = 0
            num = ''
            op = '+'
            for item in path:
                if item != '+' and item != '-':
                    num = num + item
                if item == '+':
                    if op == '+':
                        total += int(num)
                    else:
                        total -= int(num)
                    op = '+'
                    num = ''
                if item == '-':
                    if op == '+':
                        total += int(num)
                    else:
                        total -= int(num)
                    op = '-'
                    num = ''
            if op == '+':
                total += int(num)
            else:
                total -= int(num)

            return total


        # -----------------  MAIN  ----------------- #
        res = []
        def helper(num, target, path):

            if num == '':
                total = caculate(path)
                if total == target:
                    res.append(path[1:])
                    return

            for i in range(0, len(num)):

                if isNum(num[:i+1]) == True:  # 这个string可以转为int

                    # 分别尝试加法、减法、乘法三个操作
                    # 加法
                    path = path + '+' + num[:i+1]
                    helper(num[i+1:], target, path)
                    path = path[:i]  # 是因为要把那个运算符pop掉

                    # 减法
                    path = path + '-' + num[:i+1]
                    helper(num[i+1:], target, path)
                    path = path[:i+1]

                    # 乘法
                    path = path + '*' + num[:i+1]
                    helper(num[i+1:], target, path)
                    path = path[:i]

                else:
                    break

        helper(num, target, '')

        return res


s = Solution()
print s.addOperators('123',6)