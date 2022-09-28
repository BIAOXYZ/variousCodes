class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        
        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False
        
        ch = s1[0]
        for i in range(n2):
            if s2[i] == ch:
                if s2[i:] + s2[:i] == s1:
                    return True
        return False
        
"""
https://leetcode.cn/submissions/detail/368305418/

2 / 31 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    ch = s1[0]
Line 8 in isFlipedString (Solution.py)
    ret = Solution().isFlipedString(param_1, param_2)
Line 44 in _driver (Solution.py)
    _driver()
Line 55 in <module> (Solution.py)
最后执行的输入：
""
""
"""
