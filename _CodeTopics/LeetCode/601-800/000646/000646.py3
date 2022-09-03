class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key = lambda x : (x[1], x[0]))
        res = 1
        n = len(pairs)
        pre = pairs[0]
        for i in range(1, n):
            cur = pairs[i]
            if cur[0] > pre[1]:
                res += 1
                pre = cur
        return res
        
"""
https://leetcode.cn/submissions/detail/358515067/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
64.67%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
41.70%
的用户
通过测试用例：
205 / 205
"""
