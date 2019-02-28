# coding: utf-8

def function(nums):
    max_ret = 0
    ret = 0
    for item in nums:
        if item != 0:
            ret += 1
        elif ret > max_ret:
            max_ret = ret
            ret = 0
        else:
            continue

    return max_ret

print function( [0,1,1,1,0,1,1,1,1,0,0] )