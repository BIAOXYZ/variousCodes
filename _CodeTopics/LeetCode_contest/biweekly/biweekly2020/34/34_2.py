class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s) 
        n = s.count('1')
        
        if n == 0:
            # 此时结果是n-1个空隙插两个挡板，为C_{n-1}^2。
            return ((length - 1) * (length - 2) / 2) % (10**9 + 7)
        elif n % 3 != 0:
            return 0
        else:
            interval = n / 3
        
        ind = []
        for i in range(length):
            if s[i] == '1':
                ind.append(i)
        
        return (ind[interval] - ind[interval - 1]) * (ind[2*interval] - ind[2*interval - 1]) % (10**9 + 7)
    
"""
https://leetcode-cn.com/submissions/detail/105133735/

161 / 161 个通过测试用例
状态：通过
执行用时: 176 ms
内存消耗: 16.8 MB
"""
