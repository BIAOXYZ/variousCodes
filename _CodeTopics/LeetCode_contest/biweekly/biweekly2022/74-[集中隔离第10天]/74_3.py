class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        summ = sum(nums)
        reduced = 0
        nums2 = [-num for num in nums]
        heapq.heapify(nums2)
        
        while 2 * reduced < summ:
            res += 1
            curr = (-1) * heapq.heappop(nums2)
            reduced += curr * 0.5
            heapq.heappush(nums2, -curr * 0.5)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/286055179/

51 / 51 个通过测试用例
状态：通过
执行用时: 1056 ms
内存消耗: 24.1 MB
"""
