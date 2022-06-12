class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        # 手动狗头题
        return sum(heights[i] != sorted(heights)[i] for i in range(len(heights)))
        
"""
https://leetcode.cn/submissions/detail/324578191/

执行用时：
44 ms
, 在所有 Python3 提交中击败了
16.21%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
41.71%
的用户
通过测试用例：
81 / 81
"""
