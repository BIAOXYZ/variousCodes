class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n = len(s)
        for i in range(n):
            if goal == s[i:] + s[:i]:
                return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/295977713/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
59.84%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
10.30%
的用户
通过测试用例：
47 / 47
"""
