class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        length = len(timeSeries)
        if length == 0:
            return 0
        
        start = timeSeries[0]
        res = 0
        for i in range(1, length):
            end = start + duration
            if timeSeries[i] >= end:
                res += duration
            else:
                res += timeSeries[i] - start
            start = timeSeries[i]
        res += duration
        return res
        
"""
https://leetcode-cn.com/submissions/detail/237190488/

执行用时：28 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了28.95%的用户
通过测试用例：
38 / 38
"""
