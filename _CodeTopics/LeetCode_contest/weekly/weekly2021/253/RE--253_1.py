class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        
        w = ''
        i = 0
        while len(w) < len(s):
            w += words[i]
            i += 1
        if w == s:
            return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/204484244/

9 / 346 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    w += words[i]
Line 12 in isPrefixString (Solution.py)
    ret = Solution().isPrefixString(param_1, param_2)
Line 43 in _driver (Solution.py)
    _driver()
Line 53 in <module> (Solution.py)
最后执行的输入：
"ccccccccc"
["c","cc"]
"""
