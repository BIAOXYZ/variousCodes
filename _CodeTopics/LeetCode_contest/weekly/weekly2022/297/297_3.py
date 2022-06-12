class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(cookies)
        res = [float('inf')]
        
        tmp = [0] * k
        def backtrack(ind):
            if ind == n:
                res[0] = min(res[0], max(tmp))
                return
            for i in range(k):
                tmp[i] += cookies[ind]
                backtrack(ind+1)
                tmp[i] -= cookies[ind]
        
        backtrack(0)
        return res[0]
    
"""
https://leetcode.cn/submissions/detail/324351068/

34 / 34 个通过测试用例
状态：通过
执行用时: 7764 ms
内存消耗: 13.1 MB
"""
