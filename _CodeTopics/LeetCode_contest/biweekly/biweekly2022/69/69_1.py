class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
        res = ''
        title = title.split()
        for s in title:
            if len(s) <= 2:
                s = s.lower()
            else:
                s = s.lower()
                s = s[0].upper() + s[1:]
            res += s + ' '
        return res[:-1]
    
"""
https://leetcode-cn.com/submissions/detail/256382667/

200 / 200 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 13.3 MB
"""
