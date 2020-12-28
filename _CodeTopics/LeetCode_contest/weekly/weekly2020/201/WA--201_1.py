class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 核心点就是单个相邻的大小写/小大写字母必须删除。
        
        length = len(s)
        if length == 0 or length == 1:
            return s
        
        def iscapital(let):
            if ord(let) >= ord('A') and ord(let) <= ord('Z'):
                return True
            return False
        
        res = []
        for i in range(length):
            if not res:
                res.append(s[i])
            elif iscapital(s[i]) == iscapital(res[-1]):
                res.append(s[i])
            else:
                res.pop()
        return ''.join(res)
    
"""
https://leetcode-cn.com/submissions/detail/96175328/

153 / 334 个通过测试用例
	状态：解答错误

输入： "mC"
输出： ""
预期： "mC"
"""
