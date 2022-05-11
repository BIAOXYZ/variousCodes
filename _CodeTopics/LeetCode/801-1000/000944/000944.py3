class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        m, n = len(strs), len(strs[0])
        res = 0
        for j in range(n):
            col = [strs[i][j] for i in range(m)]
            if col != sorted(col):
                res += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/312340158/

执行用时：
116 ms
, 在所有 Python3 提交中击败了
73.68%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
53.99%
的用户
通过测试用例：
85 / 85
"""
