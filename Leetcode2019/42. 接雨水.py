# coding: utf-8

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 此题没想出来，看的解析，需要复习一下

class Solution(object):

    def trap(self, height):

        if len(height) > 2:

            # 首先找到最大值，和最大值的index，如果有相同的最大值，取左边的
            max_value = max(height)
            value_index = height.index(max_value)

            v = 0

            # 遍历从0到value_index之间的区域
            for i in range(1, value_index):
                if height[i] >= height[0]:
                    # 如果非单调减，height[0]表示左标志位
                    height[0] = height[i]
                else:
                    v = v + height[0] - height[i]

            # 遍历最右到value_index之间的区域
            for i in range(2, len(height) - value_index):
                if height[-i] >= height[-1]:
                    # 如果（从右向左看）非单调减，height[0]表示左标志位
                    height[-1] = height[-i]
                else:
                    v = v + height[-1] - height[-i]

            return v


        else:
            return 0


s = Solution()
print s.trap([5,2,1,2,1,6,0,3])
print s.trap([5,4,1,2])
print s.trap([5,4,7,3,6,4,2,7,4,2])
print s.trap([0,1,2,3,4,5,6,7])
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])