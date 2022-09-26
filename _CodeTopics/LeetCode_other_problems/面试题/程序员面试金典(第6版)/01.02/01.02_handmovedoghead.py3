class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:

        # 手动狗头题
        return sorted(s1) == sorted(s2)
        
"""
https://leetcode.cn/submissions/detail/367558716/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
33.90%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
12.08%
的用户
通过测试用例：
23 / 23
"""
