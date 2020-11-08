class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        tmp = [0 for i in range(n+1)]
        tmp[1] = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                tmp[i] = tmp[i/2]
            else:
                tmp[i] = tmp[i/2] + tmp[i/2 + 1]
        return max(tmp)
    
"""
https://leetcode-cn.com/submissions/detail/121813764/

101 / 101 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB
"""
