class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # 手动狗头题
        return any(s[i:] + s[:i] == goal for i in range(len(s)))
        
"""
https://leetcode-cn.com/submissions/detail/295977804/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
29.86%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
43.29%
的用户
通过测试用例：
47 / 47
"""
