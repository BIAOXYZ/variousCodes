class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # 手动狗头题
        return (sorted(nums)[-1]-1) * (sorted(nums)[-2]-1)
        
"""
https://leetcode.cn/submissions/detail/355112587/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.42%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
10.31%
的用户
通过测试用例：
104 / 104
"""
