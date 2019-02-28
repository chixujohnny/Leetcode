# coding: utf-8

# h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）至多有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）”

# 输入: citations = [3,0,6,1,5]
# 输出: 3
# 解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

# 比较考智力，这个题可以背一下

class Solution(object):

    def hIndex(self, citations):

        # 先升序排序，再扫一遍，时间复杂度O(nlogn)
        citations.sort(reverse=True)
        len_c = len(citations)
        h = 0
        for i in range(len_c):
            if citations[i] >= i+1:
                h += 1

        return h



s = Solution()
print s.hIndex([3,0,6,1,5])