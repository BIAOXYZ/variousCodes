class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        diffArr = [0 for _ in range(n+1)]
        for first, last, seats in bookings:
            diffArr[first] += seats
            if last < n:
                diffArr[last+1] -= seats
        
        for i in range(1, n+1):
            diffArr[i] += diffArr[i-1]
        diffArr.pop(0)
        return diffArr
        
"""
https://leetcode-cn.com/submissions/detail/213232742/

63 / 63 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 23 MB

执行用时：100 ms, 在所有 Python 提交中击败了81.08%的用户
内存消耗：23 MB, 在所有 Python 提交中击败了18.92%的用户
"""
