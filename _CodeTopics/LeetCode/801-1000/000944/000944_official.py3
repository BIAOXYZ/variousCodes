class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        # official
        return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))  # 空间复杂度为 O(m)，改用下标枚举可以达到 O(1)
        
"""
https://leetcode.cn/submissions/detail/312342090/

执行用时：
108 ms
, 在所有 Python3 提交中击败了
75.44%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
40.35%
的用户
通过测试用例：
85 / 85
"""
