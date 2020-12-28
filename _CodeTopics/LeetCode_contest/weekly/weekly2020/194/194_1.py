class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res
    
"""
https://leetcode-cn.com/contest/weekly-contest-194/submissions/detail/80711509/

54 / 54 个通过测试用例
	状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
