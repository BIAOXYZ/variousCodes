class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        first = 0
        for ch in s:
            tmp = ord(ch) - ord('a') + 1
            if tmp < 10:
                first += tmp
            else:
                first += tmp % 10 + tmp / 10
        ##print first
        if k == 1: return first
        
        
        res = 0
        while k > 1:
            k -= 1
            while first > 0:
                res += first % 10
                first /= 10
            if k == 1:
                return res
            else:
                first = res
                res = 0
                
"""
https://leetcode-cn.com/submissions/detail/199503647/

216 / 216 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB
"""
