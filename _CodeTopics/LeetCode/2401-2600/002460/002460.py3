class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        res, n_zeros = [], 0
        for num in nums:
            if num != 0:
                res.append(num)
            else:
                n_zeros += 1
        return res + [0] * n_zeros
        
"""
https://leetcode.cn/submissions/detail/437714292/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
79.52%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
16.87%
的用户
通过测试用例：
36 / 36
"""
