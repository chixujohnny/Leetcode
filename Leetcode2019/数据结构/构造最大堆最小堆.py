# coding:utf-8

# 最大堆：根节点键值为所有键值最大者，每个节点的值都比其孩子的值大
# 最小堆：根节点键值为所有键值最小者，每个节点的值都比其孩子的值小

# 构造完全二叉树  教程见：https://blog.csdn.net/chengde6896383/article/details/81121113
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

l = [4,1,3,2,16,9,10,14,8,7]
stack = []
top = TreeNode(l[0])
l.pop(0)
while len(l) != 0:
    if stack == []:
        root = top
    else:
        root = stack[0]
        stack.pop(0)
    root.left = TreeNode(l[0])
    stack.append(root.left)
    l.pop(0)
    if len(l) == 0: break
    root.right = TreeNode(l[0])
    stack.append(root.right)
    l.pop(0)

# BFS打印完全二叉树  队列
queue = [top]
print top.val
while queue != []:
    root = queue[0]
    queue.pop(0)
    if root.left != None:
        print root.left.val
        queue.append(root.left)
    if root.right != None:
        print root.right.val
        queue.append(root.right)

# DFS打印完全二叉树  栈
stack = [top]
print top.val
while stack != []:
    root = stack[-1]
    stack.pop(-1)
    if root.left != None:
        print root.left.val
        stack.append(root.left)
    if root.right != None:
        print root.right.val
        stack.append(root.right)

# 最大堆构造
# 视频教程：https://www.bilibili.com/video/av47196993?from=search&seid=5519025253258454054
tree = [4,1,3,2,16,9,10,14,8,7]  # 完全二叉树的list形式

def swap(tree, max, i):  # 对max和i做交换，两者都是index
    temp = tree[max]
    tree[max] = tree[i]
    tree[i] = temp

def heapify(tree, n, i):  # n是tree的长度，i是该父节点
    #  设置递归出口
    if i >= n:
        return

    left = 2*i+1   # 左孩子
    right = 2*i+2  # 右孩子
    max = i
    if left < n and tree[left] > tree[max]:
        max = tree[left]
    if right < n and tree[right] > tree[max]:
        max = tree[right]
    if max != i:
        swap(tree, max, i)
        heapify(tree, n, max)

def build_heap(tree, n):
    last_node = n - 1
    parent_node = (last_node - 1) / 2
    # 对全部的parent_node做一下heapify就可以了
    i = parent_node
    while i >= 0:
        heapify(tree, n, parent_node)
        i -= 1