class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        for num in nums:
            num.sort()
        res = 0
        for col in zip(*nums):
            res += max(col)
        return res
        
"""
https://leetcode.cn/submissions/detail/444103482/

执行用时：
88 ms
, 在所有 Python3 提交中击败了
97.37%
的用户
内存消耗：
33.4 MB
, 在所有 Python3 提交中击败了
13.26%
的用户
通过测试用例：
1057 / 1057
"""
