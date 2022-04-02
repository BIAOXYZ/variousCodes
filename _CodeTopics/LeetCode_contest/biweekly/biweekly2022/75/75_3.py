class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        
        # 本来这些都是 [0] * n 的数组，后来发现数组反而不对。
        
        dp0 = 0
        dp01 = 0
        dp010 = 0
        for i, ch in enumerate(s):
            if ch == '0':
                dp0 += 1
                if i >= 2:
                    dp010 = dp010 + dp01
            elif ch == '1':
                if i >= 1 and dp0 > 0:
                    dp01 = dp01 + dp0
        
        dp1 = 0
        dp10 = 0
        dp101 = 0
        for i, ch in enumerate(s):
            if ch == '1':
                dp1 += 1
                if i >= 2:
                    dp101 = dp101 + dp10
            elif ch == '0':
                if i >= 1 and dp1 > 0:
                    dp10 = dp10 + dp1
        
        return dp010 + dp101
    
"""
https://leetcode-cn.com/submissions/detail/293891678/

107 / 107 个通过测试用例
状态：通过
执行用时: 812 ms
内存消耗: 13.7 MB
"""
"""
这题原来代码是这么写的（后来发现dp如果用数组反而不对，于是赶紧改成了用单个变量）：

class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        ind0 = [ind for ind, ch in enumerate(s) if ch == '0']
        ind1 = [ind for ind, ch in enumerate(s) if ch == '1']
        if not ind0 or not ind1: return 0
        
        dp0 = [0] * n
        dp01 = [0] * n
        dp010 = [0] * n
        for i, ch in enumerate(s):
            if ch == '0':
                dp0[i] = dp0[i-1] + 1
                if i >= 2:
                    dp010[i] = dp010[i-1] + dp01[i-1]
            elif ch == '1':
                if i >= 1 and dp0[i-1] > 0:
                    dp01[i] = dp01[i-1] + dp0[i-1]
        
        dp1 = [0] * n
        dp10 = [0] * n
        dp101 = [0] * n
        for i, ch in enumerate(s):
            if ch == '1':
                dp1[i] = dp1[i-1] + 1
                if i >= 2:
                    dp101[i] = dp101[i-1] + dp10[i-1]
            elif ch == '0':
                if i >= 1 and dp1[i-1] > 0:
                    dp10[i] = dp10[i-1] + dp1[i-1]
        
        return dp010[n-1] + dp101[n-1]
"""
