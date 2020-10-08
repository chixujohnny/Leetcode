# coding: utf-8

# 出处见：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

# l = [[7,None], [13,0], [11,4], [10,2], [1,0]]
l = [[Node(7),None], [Node(13),0], [Node(11),4], [Node(10),2], [Node(1),0]]

