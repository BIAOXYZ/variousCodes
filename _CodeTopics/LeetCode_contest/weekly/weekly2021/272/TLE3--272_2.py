class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        
        n = len(spaces)
        n1 = len(s)
        spaces = [spaces[i] + i for i in range(n)]
        
        used = 0
        res = ''
        for i in range(n + n1):
            if i in spaces:
                res += ' '
                used += 1
            else:
                res += s[i - used]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/249859238/

58 / 66 个通过测试用例
状态：超出时间限制
"""
