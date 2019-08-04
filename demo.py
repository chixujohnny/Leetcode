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

a = [[1], [2]]
b = [3]
print a.append(b[:])