class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # 排序后利用贪心算法思想，优先满足前面的气球（线段区间），同时对于下一个
        # 线段区间point，不断根据新计算的交集结果的情况，决定是否在总结果上加1。
        # 如果交集为空，说明新的线段区间需要一只箭，所以res加上1，并且下次要用到的交集就变成了这个新区间point。
        # 如果交集结果不为空，那么不需要额外的箭，但是下次要用到的交集必须更新成包含point影响的部分，也就是更新成tmp。

        def list_intersection(l1, l2):
            if not l1 or not l2 or l1[0] > l2[1] or l2[0] > l1[1]:
                return []
            return [max(l1[0], l2[0]), min(l1[1], l2[1])]

        points.sort(key = lambda x: (x[0], x[1]))
        res = 0
        currIntersetion = []

        for point in points:
            tmp = list_intersection(currIntersetion, point)
            if tmp == []:
                res += 1
                currIntersetion = point
            else:
                currIntersetion = tmp
        return res
        
"""
https://leetcode-cn.com/submissions/detail/125484307/

45 / 45 个通过测试用例
状态：通过
执行用时: 124 ms
内存消耗: 17.1 MB

执行用时：124 ms, 在所有 Python 提交中击败了78.24%的用户
内存消耗：17.1 MB, 在所有 Python 提交中击败了75.49%的用户
"""
