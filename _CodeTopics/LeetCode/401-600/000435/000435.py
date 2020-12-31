class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        def has_intersection(l1, l2):
            return True if l2[0] < l1[1] else False

        length = len(intervals)
        if length <= 1:
            return 0
        
        intervals.sort(key=lambda x : (x[0], x[1]))
        res = 0
        cur = intervals[0]
        for i in range(1, length):
            if not has_intersection(cur, intervals[i]):
                cur = intervals[i]
            else:
                res += 1
                cur = cur if cur[1] <= intervals[i][1] else intervals[i]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/135105627/

18 / 18 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 16.8 MB

执行用时：64 ms, 在所有 Python 提交中击败了35.07% 的用户
内存消耗：16.8 MB, 在所有 Python 提交中击败了5.80% 的用户
"""
