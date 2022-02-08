class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        length = len(nums)
        res = 0
        for i in range(length-1):
            for j in range(i+1, length):
                res += 1 if abs(nums[i] - nums[j]) == k else 0
        return res
        
"""
https://leetcode-cn.com/submissions/detail/266057296/

执行用时：200 ms, 在所有 Python3 提交中击败了18.96%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.08%的用户
通过测试用例：
237 / 237
"""
