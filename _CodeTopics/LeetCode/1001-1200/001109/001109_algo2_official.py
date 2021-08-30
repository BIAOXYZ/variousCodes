class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        # 官方答案，但是我觉得下标处理的不够好，等会写个更自然的试试。

        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
        return nums
        
"""
https://leetcode-cn.com/submissions/detail/213232292/

63 / 63 个通过测试用例
状态：通过
执行用时: 96 ms
内存消耗: 22.9 MB

执行用时：96 ms, 在所有 Python 提交中击败了87.84%的用户
内存消耗：22.9 MB, 在所有 Python 提交中击败了22.97%的用户
"""
