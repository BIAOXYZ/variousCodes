class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # 核心点就是单个相邻的大小写/小大写字母必须删除。   
        
        length = len(s)
        if length < 2:
            return s
        
        res = []
        for i in range(length):
            if not res:
                res.append(s[i])
            elif abs(ord(s[i]) - ord(res[-1])) % 32 != 0:
                res.append(s[i])
            else:
                if s[i] == res[-1]:
                    res.append(s[i])
                else:
                    res.pop()
            #print res
        return ''.join(res)
    
"""
https://leetcode-cn.com/submissions/detail/96190916/

334 / 334 个通过测试用例
	状态：通过
执行用时：20 ms
内存消耗：12.8 MB
"""
