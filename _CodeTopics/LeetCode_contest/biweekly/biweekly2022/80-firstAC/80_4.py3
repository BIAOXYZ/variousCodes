class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        prefixSum = list(accumulate(nums))
        ## print(prefixSum)
        
        n = len(nums)
        res = 0
        for i in range(n):
            left, right = i, n-1
            ind = -1
            while left <= right:
                mid = left + (right - left) // 2
                subSum = prefixSum[mid] - prefixSum[i] + nums[i]
                subLen = mid - i + 1
                if subSum * subLen >= k:
                    right = mid - 1
                else:
                    ind = mid
                    left = mid + 1
            if ind != -1:
                res += ind - i + 1
        return res
    
"""
https://leetcode.cn/submissions/detail/324233873/

167 / 167 个通过测试用例
状态：通过
执行用时: 3048 ms
内存消耗: 26.7 MB
"""
