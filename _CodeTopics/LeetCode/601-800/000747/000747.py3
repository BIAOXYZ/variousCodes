class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        maxNum, secondMaxNum = sorted(nums)[-1], sorted(nums)[-2]
        return nums.index(maxNum) if maxNum >= 2 * secondMaxNum else -1
        
"""
https://leetcode-cn.com/submissions/detail/257867637/

执行用时：32 ms, 在所有 Python3 提交中击败了67.31%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了85.71%的用户
通过测试用例：
232 / 232
"""
