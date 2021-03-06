class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 0:
            remainder = n % 3
            if remainder == 2:
                return False
            n /= 3
        return True
    
"""
https://leetcode-cn.com/submissions/detail/151900755/

128 / 128 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.9 MB
"""
