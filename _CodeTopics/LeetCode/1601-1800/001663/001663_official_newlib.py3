class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = []
        for i in range(1, n + 1):
            lower = max(1, k - (n - i) * 26)
            k -= lower
            s.append(ascii_lowercase[lower - 1])
        return ''.join(s)
    
"""
https://leetcode.cn/submissions/detail/397265351/

执行用时：
952 ms
, 在所有 Python3 提交中击败了
25.46%
的用户
内存消耗：
16.9 MB
, 在所有 Python3 提交中击败了
33.77%
的用户
通过测试用例：
94 / 94
"""
