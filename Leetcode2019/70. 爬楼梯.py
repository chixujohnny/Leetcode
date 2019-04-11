# coding: utf-8

# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 注意：这道题不能用递归做，因为中间会有很多重复计算，通不过的，找规律就好

class Solution(object):

    def climbStairs(self, n):

        s = [1,1,2]
        if n <= 2:
            return s[n]
        for i in range(3, n+1):
            s.append(s[i-1] + s[i-2])
        return s[-1]

s = Solution()
print s.climbStairs(6)