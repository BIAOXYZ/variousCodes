class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        # 量级是 2 * 10^4，应该二重for循环超时的可能性还是大于 50%？

        res = [0 for _ in range(n)]
        for first, last, seats in bookings:
            for ind in range(first, last+1):
                res[ind-1] += seats
        return res
        
"""
https://leetcode-cn.com/submissions/detail/213227607/

46 / 63 个通过测试用例
状态：超出时间限制
"""
"""
果然超时了，所以二重for循环的话，量级应该最多是 10*4 ？
"""
