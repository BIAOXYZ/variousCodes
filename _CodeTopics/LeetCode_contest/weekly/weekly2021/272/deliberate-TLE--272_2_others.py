class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """

        ans = ""
        idx = 0
        tmp = list(s)
        for i, k in enumerate(tmp):
            if idx < len(spaces) and i == spaces[idx]:
                idx += 1
                ans += " "
            ans += k
        return ans
        
"""
https://leetcode-cn.com/submissions/detail/249898560/

59 / 66 个通过测试用例
状态：超出时间限制
"""
