class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        res = total = 0
        for ch in s:
            if ch == '(':
                total += 1
            else:
                total -= 1
            if total == -1:
                res += 1
                total = 0
        if total > 0:
            res += total
        return res
        
"""
https://leetcode.cn/submissions/detail/369753638/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
49.57%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
25.74%
的用户
通过测试用例：
115 / 115
"""
