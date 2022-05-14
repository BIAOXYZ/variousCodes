class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
        s = str(num)
        n = len(s)
        res = 0
        for i in range(n-k+1):
            if int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0:
                res += 1
        return res
    
"""
https://leetcode.cn/submissions/detail/313506459/

183 / 183 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 12.8 MB
"""
