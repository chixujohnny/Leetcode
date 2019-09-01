class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 2:
            return 1

        def cP(n):
            List = n*[1]
            if n < 3:
                return 0
            List[0], List[1] = 0, 0
            for i in range(2, int(n ** 0.5) + 1):
                if List[i] == 1:
                    List[i * i:n:i] = [0] * len(List[i * i:n:i])
            return sum(List)

        zhishu_num = cP(n+1)
        others_num = n - zhishu_num

        l = 1
        for i in range(1, zhishu_num+1):
            l = l * i

        r = 1
        for i in range(1, others_num+1):
            r = r * i

        return (l * r) % (10**9 + 7)

        # if l * r > 10**9 + 7:
        #     return (l * r) % (10**9 + 7)
        # else:
        #     return l * r


s = Solution()
print s.numPrimeArrangements(100)