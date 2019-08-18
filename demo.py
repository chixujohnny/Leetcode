# coding: utf-8

# a = 'BANC'
# b = 'ABC'
# print b.split('')
# if set(b) in set(a):
#     print 'ok'


# import numpy as np
# import keras
# from sklearn.preprocessing import LabelEncoder

# a = ['apple','banana','banana','tomato','carrot']
# encoder = LabelEncoder()
# encoder.fit(a)
# a_encoder = encoder.transform(a)
# print a_encoder
# num_classes = np.max(a_encoder)+1
# print num_classes
# a_encoder = keras.utils.to_categorical(a_encoder, num_classes)
# print a_encoder

# print [1] + [0,0,0,0]

# a = [2,3,4]
# a.append(None)
# a.append(3)
# print a

# print [4,3,4,5] + [0]
# print sum([1,2,3,4])

# print [[]] + [[1,2,3]]

# # a = [[1],[2],[3]]
# a = [1,2,3]
# a = a.reverse()
# print a

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
#
# head_slow = head
# head_fast = head
#
# while head_fast != None and head_fast.next != None:
#     head_slow = head_slow.next
#     head_fast = head_fast.next.next
#
# print head_slow.val

# print [1,2,3].append([1])

# a = [[1], [2]]
# b = [3]
# print a.append(b[:])


# coding: utf-8
# coding: utf-8

# coding: utf-8
import copy


# class Solution(object):
#     def movesToMakeZigzag(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         nums = [float("inf")] + nums + [float("inf")]
#
#         # 奇数位小于两边
#         res_ji = 0
#         for i in range(1, len(nums)-1):
#             if nums[i] >= min(nums[i - 1], nums[i + 1]) and i%2==0:
#                 res_ji += abs(min(nums[i - 1], nums[i + 1]) - nums[i]) + 1
#
#         # 偶数位小于两边
#         res_ou = 0
#         for i in range(1, len(nums)-1):
#             if nums[i] >= min(nums[i - 1], nums[i + 1]) and i%2==1:
#                 res_ou += abs(min(nums[i - 1], nums[i + 1]) - nums[i]) + 1
#
#         return min(res_ji, res_ou)
#
# s = Solution()
# # print s.movesToMakeZigzag([1,2,3])
# # print s.movesToMakeZigzag([9,6,1,6,2])
# print s.movesToMakeZigzag([10,4,4,10,10,6,2,3])



# def function(nums, target):
#     dp = [0] * (target+1)
#
#     dp[0] = 1
#
#     for i in range(1, target + 1):
#         for j in range(len(nums)):
#             if i >= nums[j]:
#                 dp[i] += dp[i - nums[j]]
#
#
# print function([1,2,3], 4)

# nums = [1,2,3]
# i = 2
# print nums[:i] + nums[i+1:]

# dp = [[0]*10] * 3
# print dp

a = [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","0","1"],["1","0","1","1","1"]]]
for item in a:
    item += item
print item