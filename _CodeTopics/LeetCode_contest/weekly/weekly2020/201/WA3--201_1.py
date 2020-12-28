class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 核心点就是单个相邻的大小写/小大写字母必须删除。   
        
        def iscapital(let):
            if ord(let) >= ord('A') and ord(let) <= ord('Z'):
                return True
            return False
        
        length = len(s)
        if length < 2:
            return s
        if length == 2:
            if iscapital(s[0]) and not iscapital(s[1]):
                return ''
            else:
                return s
        
        res = []
        for i in range(length):
            if not res:
                res.append(s[i])
            elif iscapital(s[i]) == iscapital(res[-1]):
                res.append(s[i])
            else:
                res.pop()
            #print res
        return ''.join(res)
    
"""
https://leetcode-cn.com/submissions/detail/96182876/

154 / 334 个通过测试用例
	状态：解答错误

输入： "Hvh"
输出： "h"
预期： "Hvh"
"""
