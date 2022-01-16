class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        n = len(s)
        i = 0
        res = []
        while i < n:
            res.append(s[i:i+k])
            i += k
        if n % k == 0:
            return res
        res[-1] = res[-1] + (k - n % k) * fill
        return res
    
"""
https://leetcode-cn.com/submissions/detail/258921232/

157 / 157 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB
"""
