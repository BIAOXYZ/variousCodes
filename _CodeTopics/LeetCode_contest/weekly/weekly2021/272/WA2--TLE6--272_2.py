class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        n = len(spaces)
        res = ''
        for i in range(n):
            if i == 0:
                if spaces[i] == 0:
                    res += ' '
                else:
                    res += s[:spaces[i]] + ' '
            else:
                res += s[spaces[i-1]:spaces[i]] + ' '
        res += s[spaces[n-1]:]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/249897035/

62 / 66 个通过测试用例
状态：超出时间限制
"""
