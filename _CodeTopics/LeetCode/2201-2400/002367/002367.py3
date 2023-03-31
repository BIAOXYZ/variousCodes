class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    res += int(nums[j] - nums[i] == nums[k] - nums[j] == diff)
        return res
        
"""
https://leetcode.cn/submissions/detail/419852905/

执行用时：
2984 ms
, 在所有 Python3 提交中击败了
5.20%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
18.90%
的用户
通过测试用例：
104 / 104
"""
