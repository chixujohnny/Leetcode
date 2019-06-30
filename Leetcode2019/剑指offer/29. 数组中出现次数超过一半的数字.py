# coding: utf-8

# 某个数字出现的次数超过了这个数组长度的一半，请找出这个数字

# 解法：根据数组特点找出O(n)的算法
# 这个数字出现的次数比其他所有数字出现次数之和还要多
# 如果遍历到下一个数字的时候，还是上一个数字，则次数+1，反之-1
# 如果次数变成了0，则将目前的数字设为待返回数字，times=1
# 这样，最后剩下的数字（times>=1）也就是我们想要的数字

def function(data):
    ret = data[0]
    times = 1
    for i in range(1, len(data)):
        if data[i] == ret:
            times += 1
        else:
            times -= 1
            if times == 0:
                ret = data[i]
                times = 1
    return ret

if __name__ == '__main__':
    data = [1,2,3,2,2,2,5,4,2]
    print function(data)