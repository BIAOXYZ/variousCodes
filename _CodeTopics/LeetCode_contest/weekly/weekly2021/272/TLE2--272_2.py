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
        lis = [''] * (n + n1)
        for i in range(n + n1):
            if i in spaces:
                lis[i] = ' '
                used += 1
            else:
                lis[i] = s[i - used]
        return ''.join(lis)
    
"""
https://leetcode-cn.com/submissions/detail/249849833/

59 / 66 个通过测试用例
状态：超出时间限制
"""
