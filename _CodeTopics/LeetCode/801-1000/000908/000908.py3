class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        return 0 if max(nums) - min(nums) <= 2*k else max(nums) - min(nums) - 2*k
        
"""
https://leetcode-cn.com/submissions/detail/307387936/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
22.95%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
73.19%
的用户
通过测试用例：
68 / 68
"""
