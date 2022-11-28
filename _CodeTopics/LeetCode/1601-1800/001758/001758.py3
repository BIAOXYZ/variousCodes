class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)
        res0 = res1 = 0
        lis0 = ['0' if i % 2 == 0 else '1' for i in range(n)]
        lis1 = ['1' if i % 2 == 0 else '0' for i in range(n)]
        for i in range(n):
            if s[i] != lis0[i]:
                res0 += 1
            if s[i] != lis1[i]:
                res1 += 1
        return min(res0, res1)
        
"""
https://leetcode.cn/submissions/detail/385633276/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
87.50%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
8.75%
的用户
通过测试用例：
89 / 89
"""
