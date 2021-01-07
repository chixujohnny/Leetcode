# coding: utf-8

# 4、算法题-矩阵题
# 对于一个n维整数方阵，每列去掉一个数
# 要求相邻两列所去掉的数不相邻（不在同一行）
# 问：对于任意一个给定矩阵，在所有可能的情形下，留下的数字之和的最小值
# （答题要求：请尽量使用代码作答，思路仅作为判分参考）

import numpy as np

def CreateNewMatrix(rowNum, lineNum):
    matrix = []
    for row in range(rowNum):
        matrix.append([])
        for line in range(lineNum):
            matrix[row].append(0)

    return matrix

def function(matrix):

    if len(matrix) != len(matrix[0]):
        return False

    if matrix is None or len(matrix) < 2 or len(matrix[0]) < 2:
        return 0

    # 因为处理列的运算在python list里不是很好做，所以要先把行转列，也就是做个转置
    # 这样，题干里的"列"，全部变成了"行"
    matrix = np.mat(matrix).T.tolist()

    # 先把array加工成一个新的矩阵：目标位置所处列的其余元素之和
    #
    # 例如：
    #
    #    3 5 0        5  3  8
    #    2 9 1  ==>  10  3 11
    #    8 7 4       11 12 15

    sum_matrix = CreateNewMatrix(len(matrix), len(matrix))
    for row in range(len(matrix)):
        for line in range(len(matrix)):
            tag = matrix[row][line]
            matrix[row][line] = 0
            sum_matrix[row][line] = sum(matrix[row])
            matrix[row][line] = tag

    # 再新建一个矩阵 -- DP矩阵
    DP = CreateNewMatrix(len(matrix), len(matrix))
    DP[0] = sum_matrix[0]  # 第一行直接copy sum_matrix
    for row in range(1, len(matrix)):
        for line in range(len(matrix)):
            tag = DP[row-1][line]
            DP[row - 1][line] = float('inf')
            DP[row][line] = sum_matrix[row][line] + min(DP[row-1])
            DP[row - 1][line] = tag

    return min(DP[-1])  # return最后一行里面最小的一个就行了



matrix = [[3,2,8,6],[5,9,7,1],[0,1,4,10],[1,2,5,1]]
print function(matrix)