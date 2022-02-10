class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # 排序后，以下标 i 为最小值的 k 个整数集合里，最优的选择就是：
        # i, i+1, ... i+k-1
        # 否则会取到 nums[i+k-1] 之后的某个更大的元素，使得差值可能更大。

        nums.sort()
        length = len(nums)
        res = 10**5 + 1
        for i in range(length-k+1):
            res = min(res, nums[i+k-1] - nums[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/266885140/

执行用时：44 ms, 在所有 Python3 提交中击败了63.46%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了53.08%的用户
通过测试用例：
118 / 118
"""
