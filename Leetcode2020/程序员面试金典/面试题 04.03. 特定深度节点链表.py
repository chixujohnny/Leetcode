# coding: utf-8

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def listOfDepth(self, tree):
        """
        :type tree: TreeNode
        :rtype: List[ListNode]
        """
        res, queue = [], collections.deque()
        queue.append(tree)

        while len(queue) != 0:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            res.append(tmp)

        resres = []
        for level_list in res:
            head = None
            node = None
            for item in level_list:
                if head == None:
                    head = ListNode(item)
                    node = head
                else:
                    node.next = ListNode(item)
                    node = node.next
            resres.append(head)

        return resres


treeList = [1,2,3,4,5,None,7,8]

def CreateBineryTree(root, treeList, i):

    if i < len(treeList):
        if treeList[i] == None:
            return None
        else:
            root = TreeNode(treeList[i])
            root.left  = CreateBineryTree(root.left,  treeList, 2*i+1)
            root.right = CreateBineryTree(root.right, treeList, 2*i+2)
            return root
    return root

root = CreateBineryTree(None, treeList, 0)


s = Solution()
print s.listOfDepth(root)