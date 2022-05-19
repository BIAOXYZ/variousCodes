class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)
        startArr = [0] * n
        startDic = {}
        for i, (start, _) in enumerate(intervals):
            startArr[i] = start
            startDic[start] = i
        startArr.sort()

        res = []
        for _, end in intervals:
            ind = bisect.bisect_left(startArr, end)
            res.append(startDic[startArr[ind]]) if ind != n else res.append(-1)
        return res
        
"""
https://leetcode.cn/submissions/detail/315772122/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
95.56%
的用户
内存消耗：
18.9 MB
, 在所有 Python3 提交中击败了
55.92%
的用户
通过测试用例：
19 / 19
"""
