class Solution:
    def generateTheString(self, n: int) -> str:

        return 'a'*(n-1) + 'b' if n & 1 == 0 else 'a'*n
        
"""
https://leetcode.cn/submissions/detail/344675244/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
88.30%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
73.10%
的用户
通过测试用例：
103 / 103
"""
