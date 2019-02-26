# coding: utf-8

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if len(secret) == 0:
            return '0A0B'

        a = 0
        b = 0
        secret_dict = {}

        # 扫第一轮secret确定bulls，将secret丢进hash table，如果遇到bulls直接 a += 1(此时hash table中的value值不变)
        for i, item in enumerate(secret):
            if item == guess[i]:
                a += 1
                guess = guess[:i] + ' ' + guess[i+1:]
            else:
                if secret_dict.has_key(item) == False:
                    secret_dict[item] = 1
                else:
                    secret_dict[item] += 1

        # 扫第二轮guess确定cows
        for item in guess:
            if secret_dict.has_key(item) == True and secret_dict[item] != 0:
                b += 1
                secret_dict[item] -= 1

        return str(a) + 'A' + str(b) + 'B'

s = Solution()
print s.getHint("1122", "1222")
print s.getHint("1122", "2211")
print s.getHint("1123", "0111")
print s.getHint("1807", "7810")