class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        for i in range(2, n/2+1):
            if n % i == 0:
                if i*i != n:
                    return False
                else:
                    return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/201902199/

227 / 227 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13.3 MB
"""
