# coding: utf-8


# 3、算法题-动态规划题
# 假设你有M万元（M为整数，100<M<50000），理财产品有N个（1<N<20）
# 每个产品投资额度为V0，V1···Vn-1（Vi为整数，10<Vi<50000，单位万）
# 对应期望年化率R0，R1···Rn-1。（Ri为整数，单位：元）
# 那么如何投资才能将整体收益最大化？


M = 100
V = [20, 35, 40, 10, 50]
R = [3 , 2 , 2 , 4 , 5 ]

def function(M, V, R):

    if len(R) == 0 or len(V) == 0:
        return [], 0

    # 初始化数组
    res = [0] * len(V)

    # R中每一个成员做大小的排名，并对最后的排名结果做reverse
    sorted_R = sorted(range(len(R)), key=R.__getitem__, reverse=True)  #[4, 3, 0, 1, 2]

    left = M  # 剩余可投资产
    for i in sorted_R:  # 收益率由高到低遍历，贪心算法的感觉
        if V[i] <= left:
            res[i] = V[i]
            left -= V[i]
        else:
            res[i] = left
            break

    return res, sum([res[i]*R[i] for i in range(len(res))])





print function(M, V, R)