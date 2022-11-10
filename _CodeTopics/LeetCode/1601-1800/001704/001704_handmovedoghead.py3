class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 手动狗头题
        return sum(1 for ch in s[:len(s)//2] if ch in "aeiouAEIOU") == sum(1 for ch in s[len(s)//2:] if ch in "aeiouAEIOU")
        
"""
https://leetcode.cn/submissions/detail/381073732/

执行用时：
24 ms
, 在所有 Python 提交中击败了
58.33%
的用户
内存消耗：
12.9 MB
, 在所有 Python 提交中击败了
75.00%
的用户
通过测试用例：
113 / 113
"""
