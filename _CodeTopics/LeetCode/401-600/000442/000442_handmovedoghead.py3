import collections
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # 手动狗头一把，虽然不符合题目空间复杂度的要求
        return [k for k, v in collections.Counter(nums).items() if v == 2]
        
"""
https://leetcode-cn.com/submissions/detail/310612987/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
98.25%
的用户
内存消耗：
22.5 MB
, 在所有 Python3 提交中击败了
15.86%
的用户
通过测试用例：
28 / 28
"""
