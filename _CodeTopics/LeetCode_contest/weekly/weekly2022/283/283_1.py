class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        res = []
        for col in range(ord(s[0]), ord(s[3])+1):
            for row in range(int(s[1]), int(s[4])+1):
                res.append(chr(col)+str(row))
        return res
    
"""
https://leetcode-cn.com/submissions/detail/278041028/

251 / 251 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB
"""
