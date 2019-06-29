# coding: utf-8

# 快速排序
# 思路: 设数组为l，设置key=l[0]为标志位，i=0, j=len(l)-1
# (1)   l[j]开始与key比较，遇到比key小的就互换位置，否则j--，检查i==j的话就break，不break的话进行下一步
# (2)   l[i]开始与key比较，遇到比key大的就互换位置，否则i++，检查i==j的话就break
#       上面1、2步是一趟排序Partition
#       一趟排序不会得到最终结果，只能保证key左边的数都比它小、右边的比它大，但未必排好序的。
#       再用分治思想，对key左边和右边的部分做Partition
#       用递归解比较优雅

def Change(l, key, index):
    tag = l[key]
    l[key] = l[index]
    l[index] = tag
    return l

def QuickSort(l):
    if len(l) >= 2:  # 递归入口
        key = l[0]
        left, right = [], []
        l.remove(key)
        for num in l:
            if num < key:
                left.append(num)
            else:
                right.append(num)
        return QuickSort(left) + [key] + QuickSort(right)
    else:  # 递归出口
        return l

if __name__ == '__main__':
    # l = [6,2,7,3,8,9]
    l = [9,8,7,6,5,4,3,2,1]
    l = QuickSort(l)
    print l