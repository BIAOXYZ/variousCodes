class Solution:
    def greatestLetter(self, s: str) -> str:

        for i in range(25, -1, -1):
            ch, CH = string.ascii_lowercase[i], string.ascii_uppercase[i]
            if ch in s and CH in s:
                return CH
        return ''
        
"""
https://leetcode.cn/submissions/detail/397266032/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
96.83%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
85.52%
的用户
通过测试用例：
113 / 113
"""
"""
https://leetcode.cn/submissions/detail/326779270/
"""
