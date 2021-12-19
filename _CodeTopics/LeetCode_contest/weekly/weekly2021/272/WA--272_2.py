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
            elif i == n - 1:
                res += s[spaces[i-1]:spaces[i]] + ' '
                res += s[spaces[i]:]
            else:
                res += s[spaces[i-1]:spaces[i]] + ' '
        return res
    
"""
https://leetcode-cn.com/submissions/detail/249875983/

56 / 66 个通过测试用例
状态：解答错误

最后执行的输入：
"p"
[0]
"""
