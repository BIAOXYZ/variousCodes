class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        
        n = len(spaces)
        spaces = [spaces[i] + i for i in range(n)]
        lis = list(s)
        for ind in spaces:
            lis.insert(ind, ' ')
        return ''.join(lis)
    
"""
https://leetcode-cn.com/submissions/detail/249842600/

63 / 66 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
"""
