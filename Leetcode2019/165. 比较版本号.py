# coding: utf-8

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        # 去除前置0并转为int
        def deletePreZero(item):
            for tag in item:
                if tag == '0':
                    item = item[1:]
                else:
                    break
            if item != '':
                return int(item)
            else:
                return 0

        v1, v2 = version1.split('.'), version2.split('.')
        len_diff = abs(len(v1) - len(v2))  # 版本号位数差

        #  小版本号个数不一致的，补齐小版本号个数，位数少的补 '0'
        if len_diff != 0:
            for i in range(len_diff):
                if len(v1) < len(v2):
                    v1.append('0')
                else:
                    v2.append('0')

        i = 0
        while i < len(v1):
            if deletePreZero(v1[i]) > deletePreZero(v2[i]):
                return 1
            elif deletePreZero(v1[i]) < deletePreZero(v2[i]):
                return -1
            else:
                i += 1

        return 0

s = Solution()
print s.compareVersion('7.5.2.4', '7.5.3')
print s.compareVersion('1.0.1', '1')
print s.compareVersion('0.1', '1.1')
print s.compareVersion('1.0', '1.0.0')
print s.compareVersion('1.01', '1.001')