# coding: utf-8

# 算法题-蚂蚁存活概率     （注：需给出计算/推导/分析过程）

# 一段木棍上均匀分布了n只重量均为1的蚂蚁，从左至右编号为：1，2，3，...n（1号蚂蚁在木棍左端点，n号蚂蚁在木棍右端点）
# 从某一时刻开始这些蚂蚁开始同时移动，方向随机（可以向左或者向右），速度相同
# 如果某两只蚂蚁相遇，如果重量不同的话，则大的吃掉小的，身体长大为两只蚂蚁质量之和，并继续按大的方向移动
# 如果重量相同，则向左移动的蚂蚁吃掉向右移动的，身体同样长大为两只蚂蚁的重量之和，并继续向左移动
#
# 比如现重量为4的i号蚂蚁和重量为2的j号蚂蚁相遇，结果是j号蚂蚁被吃掉
# i号蚂蚁重量成长为4+2=6并按它原来的方向移动
# 向左移动的重量为2的i号蚂蚁和向右移动的重量同样为2的j号蚂蚁相遇，则i被j吃掉，重量成长为2+2=4并继续向左移动
# 整个过程中所有蚂蚁速度一直不变，并且当达到木棍的两端时会立即折返（所以初始状态下1号必然向右移动，n号必然向左移动）
# 直到最后只剩下一只蚂蚁。
#
# 求（1）最后剩下n号蚂蚁的概率（4分）
#   （2）第k个蚂蚁的存活概率（k！=n）（6分）


def combination(n):
    results = []
    combHelper(n, 0, '', results)

    return results

def combHelper(n, i, result, results):
    if i == n:
        results.append(result)
        return

    combHelper(n, i + 1, result + '0', results)
    combHelper(n, i + 1, result + '1', results)

def prob(n):
    winners = []
    combs = combination(n - 2)
    for comb in combs:
        comb = '0' + comb + '1'
        winners.append(winner([{'dir': int(comb[i]), 'score': 1, 'id': i + 1} for i in range(len(comb))]))
        # print(comb, winners[-1])

    probs = [0] * n
    for w in winners:
        probs[w - 1] += 1

    return [prob / sum(probs) for prob in probs]


def winner(combination):
    if len(combination) == 1:
        return combination[0]['id']

    i, j = 0, 0
    # [0, i): good
    # [i, j): bad
    # j: cur
    while j < len(combination) - 1:
        if combination[j]['dir'] == 0 and combination[j + 1]['dir'] == 1:
            if combination[j]['score'] > combination[j + 1]['score']:
                combination[i] = {'dir': 0, 'score': combination[j]['score'] + combination[j + 1]['score'], 'id': combination[j]['id']}
                i += 1
                j += 2
            else:
                combination[i] = {'dir': 1, 'score': combination[j]['score'] + combination[j + 1]['score'], 'id': combination[j + 1]['id']}
                i += 1
                j += 2
        else:
            combination[i] = combination[j]
            i += 1
            j += 1

    combination[0]['dir'] = 0
    if j == len(combination) - 1:
        combination[i] = combination[j]
        i += 1

    return winner(combination[:i])


for n in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print('n={n}时，k=n的蚂蚁存活概率为{sum([1/2**i for i in range((n + 1)//2, n-1)]) + 1/2**(n-2)}')
    print('       k=[1, n]的蚂蚁存活概率为{prob(n)}')