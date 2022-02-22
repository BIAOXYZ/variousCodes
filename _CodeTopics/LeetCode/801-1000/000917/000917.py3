class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
        
"""
https://leetcode-cn.com/submissions/detail/271976338/

执行用时：32 ms, 在所有 Python3 提交中击败了74.02%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了84.60%的用户
通过测试用例：
115 / 115
"""
