class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # 手动狗头题
        return 0 if 0 in nums else 1 if sum([1 for num in nums if num < 0]) % 2 == 0 else -1
        
"""
https://leetcode.cn/submissions/detail/376815360/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
55.68%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
6.59%
的用户
通过测试用例：
76 / 76
"""
