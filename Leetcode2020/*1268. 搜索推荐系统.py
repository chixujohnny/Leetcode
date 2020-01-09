# coding: utf-8

import bisect

# products = ["mobile","mouse","moneypot","monitor","mousepad"]
# searchWord = "mouse"

# 下面是个笨方法，还是要用前缀树
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        products.sort()  # 字典序排序

        ret = []
        for i in range(len(searchWord)):
            retret = []
            for item in products:
                if item[0:i+1] == searchWord[0:i+1]:
                    retret.append(item)
                if len(retret) >= 3:
                    break
            ret.append(retret)

        return ret


s = Solution()
print s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse")
print s.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags")
print s.suggestedProducts(["havana"], "tatiana")
