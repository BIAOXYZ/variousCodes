class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals.sort(key=lambda x : (x[0], x[1]))
        res = []
        i = 0
        while i < n: 
            start, end = intervals[i]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                if j < n:
                    end = max(end, intervals[j][1])
                j += 1
            res.append([start, end])
            i = j
        return res
        
"""
https://leetcode.cn/problems/merge-intervals/submissions/460188701/

时间
详情
52ms
击败 79.48%使用 Python3 的用户
内存
详情
19.32MB
击败 33.84%使用 Python3 的用户
"""
