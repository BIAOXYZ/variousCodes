class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1: return 5
        elif n == 2: return 20
        
        module = 10**9 + 7
        dp = [0] * (n+1)
        dp[1], dp[2] = 5, 20
        
        for i in range(3, n+1):
            dp[i] = (dp[i-2] * 20) % module
        return dp[n]
    
"""
https://leetcode-cn.com/submissions/detail/192113673/

69 / 166 个通过测试用例
状态：执行出错

执行出错信息：
MemoryError
    dp = [0] * (n+1)
Line 12 in countGoodNumbers (Solution.py)
    ret = Solution().countGoodNumbers(param_1)
Line 39 in _driver (Solution.py)
    _driver()
Line 49 in <module> (Solution.py)
最后执行的输入：
806166225460393
"""
