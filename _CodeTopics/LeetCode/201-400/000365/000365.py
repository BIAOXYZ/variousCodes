class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b!=0:
                a, b = b, a%b
            return a

        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return x + y == z
        return z % gcd(x,y) == 0
        
"""
https://leetcode-cn.com/submissions/detail/171569765/

28 / 28 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.8 MB

执行用时：8 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了92.31%的用户
"""
