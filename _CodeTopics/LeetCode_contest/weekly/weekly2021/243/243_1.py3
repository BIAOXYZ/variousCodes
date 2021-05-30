class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def to_int(s):
            res = ''
            for ch in s:
                res += str(ord(ch) - ord('a'))
            return int(res)
        return to_int(firstWord) + to_int(secondWord) == to_int(targetWord)
    
"""
https://leetcode-cn.com/submissions/detail/182100614/

99 / 99 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 14.9 MB
"""
"""
还是 Python2 的 unicode 的问题，所以直接用 Python3 了。
"""
