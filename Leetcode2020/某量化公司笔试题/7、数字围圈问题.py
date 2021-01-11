# coding: utf-8

# 一个是24个数围一圈，相邻的数差不大于1，全部求和为0，问全部的正数求和最大是多少

# num = 24

def function(num):

    res = []

    def helper(num, left, path):

        if left == 0:
            res.append(path)
            return

        # 三种情况：-1 不变 +1
        # 首次递归
        if num == left:
            helper(num, left - 1, [1])
            helper(num, left - 1, [0])
            helper(num, left - 1, [-1])
        # 非首次递归
        else:
            helper(num, left - 1, path+[path[-1]+1])
            helper(num, left - 1, path+[path[-1]])
            helper(num, left - 1, path+[path[-1]-1])

        return

    helper(num, num, [])

    def PositiveSum(path):
        res = 0
        for item in path:
            if item > 0:
                res += item
        if abs(path[0] - path[-1]) <= 1:
            return res
        else:
            return float('-inf')

    max_sum = float('-inf')
    max_sum_path = []
    for path in res:
        if sum(path) == 0 and PositiveSum(path) > max_sum:
            max_sum = PositiveSum(path)
            max_sum_path = path

    return max_sum, max_sum_path


print function(12)


# 此题可以通过找规律看出来，num=24的时候，结果是36
