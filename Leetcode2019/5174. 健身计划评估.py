# coding: utf-8

# 你的好友是一位健身爱好者。前段日子，他给自己制定了一份健身计划。现在想请你帮他评估一下这份计划是否合理。
#
# 他会有一份计划消耗的卡路里表，其中 calories[i] 给出了你的这位好友在第 i 天需要消耗的卡路里总量。
#
# 一份计划的周期通常是 k 天，你需要计算他在这 k 天内消耗的总卡路里 T：
#
# 如果 T < lower，那么这份计划相对糟糕，并失去 1 分；
# 如果 T > upper，那么这份计划相对优秀，并获得 1 分；
# 否则，这份计划普普通通，分值不做变动。
# 请返回统计完所有 calories.length 天后得到的总分作为评估结果。
#
# 注意：总分可能是负数。


class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """

        resres = []
        for start in range(k):
            res = []
            for i in range(start, len(calories), k):
                if len(calories[i:i+k]) == k:
                    res.append(calories[i:i+k])
            resres.append(res)

        ret = 0
        for res in resres:
            res_tag = 0
            for item in res:
                if sum(item) < lower:
                    ret -= 1
                if sum(item) > upper:
                    ret += 1
            ret += res_tag

        return ret


s = Solution()
print s.dietPlanPerformance([6,5,0,0], 2, 1, 5)
print s.dietPlanPerformance([3,2], 2, 0, 1)
print s.dietPlanPerformance([1,2,3,4,5], 1, 3, 3)
print s.dietPlanPerformance([6,13,8,7,10,1,12,11], 6, 5, 37)