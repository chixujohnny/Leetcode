# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        res = [root.val]
        queue = [root]  # List[Treenode]

        while queue != []:
            if queue[0].left != None:
                queue.append(queue[0].left)
                res.append(queue[0].left.val)
            if queue[0].right != None:
                queue.append(queue[0].right)
                res.append(queue[0].right.val)
            queue = queue[1:]  # pop

        return res


treeList = [3,9,20,None,None,15,7]

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
print s.levelOrder(root)