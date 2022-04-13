class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        # 手动狗头题
        return max(sum(row) for row in accounts)
        
"""
https://leetcode-cn.com/submissions/detail/299683091/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
89.72%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
44.96%
的用户
通过测试用例：
34 / 34
"""
