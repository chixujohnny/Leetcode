# coding: utf-8

class Solution(object):

    # 下面是我的解答，时间复杂度O(n^2)，pass
    def canCompleteCircuit_my_answer(self, gas, cost):

        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                f = 0
                break_flag = 0
                for j in range(len(gas)):

                    if j + i < len(gas):
                        idx = j + i
                    else:
                        idx = j - len(gas) + i

                    if f + gas[idx] - cost[idx] >= 0:
                        f = f + gas[idx] - cost[idx]
                    else:
                        break_flag = 1
                        break
                if break_flag == 0:
                    return i
        return -1

    # 下面是经典答案，时间复杂度O(n)
    def canCompleteCircuit(self, gas, cost):

        tank_margin, start, min_tank_margin = 0, 0, float('inf')
        n = len(gas)
        for i in range(n):
            tank_margin += gas[i] - cost[i]
            if tank_margin < min_tank_margin:
                min_tank_margin = tank_margin
                # 这里之所以用 (i+1)%n 不用 i+1 是因为如果i=len(gas)-1 的话，那么start=0而不是start=5，这样就少了个if判断条件
                start = (i+1)%n
        if tank_margin < 0:
            return -1
        return start


s = Solution()
print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print s.canCompleteCircuit([2,3,4], [3,4,3])