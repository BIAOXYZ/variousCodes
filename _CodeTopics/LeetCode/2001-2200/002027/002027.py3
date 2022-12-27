class Solution:
    def minimumMoves(self, s: str) -> int:

        res = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "X":
                res += 1
                i += 3
            else:
                i += 1
        return res
        
"""
https://leetcode.cn/submissions/detail/391283071/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
53.18%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
28.90%
的用户
通过测试用例：
55 / 55
"""
