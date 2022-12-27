class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        left, right = 0, n-1
        while left < right and s[left] == s[right]:
            while left < right and s[left+1] == s[left]:
                left += 1
            while left < right and s[right-1] == s[right]:
                right -= 1
            left += 1
            right -= 1
        return right - left + 1 if left < right else 1 if left == right else 0
        
"""
https://leetcode.cn/submissions/detail/391421739/

执行用时：
172 ms
, 在所有 Python3 提交中击败了
17.81%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
23.29%
的用户
通过测试用例：
100 / 100
"""
