class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        tmp = [0 for i in range(n+1)]
        tmp[1] = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                tmp[i] = tmp[i/2]
            else:
                tmp[i] = tmp[i/2] + tmp[i/2 + 1]
        return tmp[n]
    
"""
https://leetcode-cn.com/submissions/detail/121812119/

3 / 101 个通过测试用例
状态：执行出错

执行出错信息：
Line 9: IndexError: list assignment index out of range
最后执行的输入：
0
"""
