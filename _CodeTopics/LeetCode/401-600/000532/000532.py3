import bisect
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if (ind := bisect.bisect_left(nums, nums[i]+k, i+1, n)) < n and nums[ind] == nums[i]+k:
                res += 1
            if ind == n:
                break
        return res
        
"""
https://leetcode.cn/submissions/detail/325725019/

执行用时：
48 ms
, 在所有 Python3 提交中击败了
64.21%
的用户
内存消耗：
15.9 MB
, 在所有 Python3 提交中击败了
92.28%
的用户
通过测试用例：
60 / 60
"""
