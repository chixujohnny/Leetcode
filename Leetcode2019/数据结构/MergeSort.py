# coding: utf-8

# 归并排序
# 一张图看懂归并排序: https://www.cnblogs.com/wyongbo/p/Devide.html

def MergeSort(data):

    if len(data) == 1 or len(data) == 0:  # 递归出口
        return data

    left  = MergeSort(data[:len(data)/2])
    right = MergeSort(data[len(data)/2:])
    ret = []

    i, j = 0, 0
    while i<len(left) or j<len(right):
        if i<len(left) and j<len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        elif j == len(right):
            ret.append(left[i])
            i += 1
        elif i == len(left):
            ret.append(right[j])
            j += 1

    return ret

if __name__ == '__main__':
    data = [2,4,7,5,8,1,3,6]
    print MergeSort(data)
