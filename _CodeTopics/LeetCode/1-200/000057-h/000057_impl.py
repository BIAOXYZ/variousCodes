class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        if not intervals:
            return [newInterval]
        """
        # 从输入测试的角度，下面这个if其实不会发生。也就是输入newInterval不会是空集。
        if not newInterval:
            return intervals
        """

        length = len(intervals)
        res = []
        left, right = newInterval[0], newInterval[1]
        flag = 'left'

        for i in range(length):
            currSmall, currBig = intervals[i][0], intervals[i][1]
            if flag == 'left':
                if left > currBig:
                    res.append(intervals[i])
                elif currSmall <= left <= currBig:
                    newleft = currSmall
                    flag = 'right'
                elif left < currSmall:
                    newleft = left
                    flag = 'right'
            if flag == 'right':
                if right < currSmall:
                    newright = right
                    res.append([newleft, newright])
                    flag = 'end'
                # 虽然确实是 000057.py 的实现更通用，也更简洁。但是我还是认为这里是没问题的。
                # 因为再仔细看看题目：intervals里的区间都是不重合的，所以下面的输入也不合法。
                # [[1,2],[3,11],[6,7],[8,10],[12,16]]
                # [4,8]
                # 因为不可能出现前一个区间的较大值（11）大于等于下一区间的较小值（6）的情况！
                elif currSmall <= right <= currBig:
                    newright = currBig
                    res.append([newleft, newright])
                    flag = 'end'
                    continue
                elif right > currBig:
                    continue
            if flag == 'end':
                res.append(intervals[i])
        
        if flag == 'left':
            res.append(newInterval)
        elif flag == 'right':
            res.append([newleft, right])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120907373/

156 / 156 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 14.9 MB

执行用时：28 ms, 在所有 Python 提交中击败了62.59%的用户
内存消耗：14.9 MB, 在所有 Python 提交中击败了5.18%的用户
"""
