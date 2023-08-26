class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals.sort(key=lambda x : (x[0], x[1]))
        res = []
        i = 0
        while i < n: 
            start, end = intervals[i]
            j = i + 1
            while j < n and intervals[j][0] <= intervals[j-1][1]:
                if j < n:
                    end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
        return res
        
"""
https://leetcode.cn/problems/merge-intervals/submissions/460188621/

解答错误
132 / 170 个通过的测试用例

最后执行的输入
[[2,3],[4,5],[6,7],[8,9],[1,10]]
"""
