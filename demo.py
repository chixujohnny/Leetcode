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
1
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

# a = [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","0","1"],["1","0","1","1","1"]]]
# for item in a:
#     item += item
# print item

# a = [1,2,3,4]
# a.reverse()
# print a


# import operator
#
#
# def topNCompetitors(numCompetitors, topNCompetitors, competitors,
#                     numReviews, reviews):
#     # WRITE YOUR CODE HERE
#
#     # using hash-table
#     competitors_dict = {}
#     for item in competitors:
#         competitors_dict[item] = 0
#
#     for review in reviews:
#         review_list = review.split(' ')
#
#         already_in = []
#         for word in review_list:
#             if competitors_dict.has_key(word) and word not in already_in:
#                 competitors_dict[word] += 1
#                 already_in.append(word)
#
#     competitors_sort = sorted(competitors_dict.items(), key=operator.itemgetter(1), reverse=True)
#
#     ret = []
#     count = -1
#     for i, item in enumerate(competitors_sort):
#         if item[1] != 0:
#             if item[1] != count:
#                 ret.append([])
#             ret[-1].append(item[0])
#
#     # sort in dictionary
#     for item in ret:
#         item.sort()
#
#     # combine
#     retret = []
#     for item in ret:
#         retret += item
#
#     return retret[:topNCompetitors]

# print topNCompetitors(5, 2, ['a','b','c','d','e'], 3, ['jife ji shub fsd a','b jifr ajh he hd hs','a frji aehu joidf efde'])
#
# retret = []
# a = ['a','b']
# c = ['b','e','f']
# print retret+a+c

# competitors_dict = {'mymarket':4, 'shopnow':2, 'newshop':2}
# competitors_sort = sorted(competitors_dict.items(), key=operator.itemgetter(1), reverse=True)
#
# ret = []
# count = -1
# for i, item in enumerate(competitors_sort):
#     if item[1] != 0:
#         if item[1] != count:
#             ret.append([])
#             count = item[1]
#         ret[-1].append(item[0])
#
# # sort in dictionary
# for item in ret:
#     item.sort()
#
# # combine
# retret = []
# for item in ret:
#     retret += item


def minimumDays(rows, columns, grid):
    # WRITE YOUR CODE HERE

    # using BFS

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    serverList = []

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                serverList.append([i, j])  # put servers into a queue

    day = 0
    while serverList != []:
        newServerList = []

        for serverNode in serverList:
            x0 = serverNode[0]
            y0 = serverNode[1]

            # traversal 4 direcitons
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]

                if 0 <= x < rows and 0 <= y < columns and grid[x][y] == 0:
                    grid[x][y] = 1
                    newServerList.append([x, y])

        if newServerList == []:
            break

        serverList = newServerList[:]
        day += 1

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 0:
                return -1

    return day

print minimumDays(4,5,[[0,1,1,0,1],[0,1,0,1,0],[0,0,0,0,1],[0,1,0,0,0]])