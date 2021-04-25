class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        res = 0
        while n >= k:
            res += n % k
            n /= k
        res += n
        return res
    
"""
https://leetcode-cn.com/submissions/detail/171647008/

65 / 65 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB
"""
