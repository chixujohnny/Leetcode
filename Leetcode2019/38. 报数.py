# coding: utf-8

# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

class Solution(object):

    def countAndSay(self, n):

        if n == 1:
            return '1'

        num = 1
        for i in range(n-1):
            num_list = []  # 将'111221' 变成 ['111','22','1']
            for item in str(num):
                if num_list == [] or num_list[-1][-1] != item:
                    num_list.append(item)
                else:
                    num_list[-1] += item
            num = ''
            for item in num_list:
                num += str(len(item))
                num += item[-1]

        return num

    # 下面是用递归方法求解
    def countAndSay_best(self, n):
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)  # !!!!递归

        count = 0  # 某个数字连续出现的次数
        temp_cha = s[0]  # 当前数字
        new_str = ""  # 新的报数序列
        for cha in s:  # 遍历旧的报数序列
            if temp_cha == cha:  # 相同连续数字累加
                count += 1
            else:  # 出现不相同数字就补充新报数序列
                new_str = new_str + str(count) + temp_cha
                temp_cha = cha  # 清零，从头累加新的数字
                count = 1
        new_str = new_str + str(count) + str(temp_cha)  # 最后一个数字补充到新报数序列中
        return new_str

s = Solution()
print s.countAndSay(6)