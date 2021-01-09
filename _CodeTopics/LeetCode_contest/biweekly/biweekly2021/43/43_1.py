class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        quotient, reminder = n / 7, n % 7
        partSum = sum(list(range(1,8)))
        startNum = 1
        
        res = 0
        for i in range(quotient):
            res += partSum
            partSum += 7
            startNum += 1
        for j in range(reminder):
            res += startNum
            startNum += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/137229132/

106 / 106 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.9 MB
"""
