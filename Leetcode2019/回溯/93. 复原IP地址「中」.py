# coding: utf-8

class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) <= 3 or len(s) > 12:
            return []

        def findDoubleZero(item):
            if item[0] == '0' and len(item)>1:
                return False
            else:
                return True

        res = []

        def helper(s, path, left):
            if len(path) == 4:
                if '' in path: return
                # 判断一下是否符合ip格式
                for item in path:
                    if int(item) > 255 or findDoubleZero(item) == False:
                        return
                res.append(path[:])
                return

            for i in range(1, 4): # 1,2,3
                left -= 1
                path.append(s[:i])
                if left == 0:  # 第3次切
                    path.append(s[i:])

                helper(s[i:], path, left)
                left += 1
                path.pop()
                if left == 1:
                    path.pop()

        helper(s, [], 3)

        ret = []
        for item in res:
            ret.append('.'.join(item))

        return ret

s = Solution()
print s.restoreIpAddresses("1212121121")