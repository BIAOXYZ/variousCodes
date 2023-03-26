class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        n = len(nums)
        se = set()
        for i in range(n-1):
            if nums[i] + nums[i+1] in se:
                return True
            se.add(nums[i] + nums[i+1])
        return False
        
"""
https://leetcode.cn/submissions/detail/418012451/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
96.43%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
92.86%
的用户
通过测试用例：
42 / 42
"""
