class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        n = len(nums)
        res = []
        if n == 0:
            return []
        
        start = 0
        while start < n:
            tmp = str(nums[start])
            end = start + 1
            while end < n and nums[end] == nums[end-1] + 1:
                end += 1
            if end - 1 > start:
                tmp += '->' + str(nums[end-1])
            res.append(tmp)
            start = end
        return res
        
"""
https://leetcode.cn/problems/summary-ranges/submissions/460146099/

时间
详情
44ms
击败 54.39%使用 Python3 的用户
内存
详情
15.64MB
击败 56.72%使用 Python3 的用户
"""
