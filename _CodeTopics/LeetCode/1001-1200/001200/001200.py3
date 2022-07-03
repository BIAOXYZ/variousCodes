class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        n = len(arr)
        arr.sort()
        minAbsDiff = float('inf')
        for i in range(1, n):
            minAbsDiff = min(minAbsDiff, abs(arr[i] - arr[i-1]))
        res = []
        for i in range(1, n):
            if minAbsDiff == abs(arr[i] - arr[i-1]):
                res.append([arr[i-1], arr[i]])
        return res
        
"""
https://leetcode.cn/submissions/detail/332313632/

执行用时：
144 ms
, 在所有 Python3 提交中击败了
19.06%
的用户
内存消耗：
25.7 MB
, 在所有 Python3 提交中击败了
39.19%
的用户
通过测试用例：
37 / 37
"""
