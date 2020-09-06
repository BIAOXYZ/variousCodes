class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        length = len(s)
        if s[0] == '?':
            s[0] = 'a'
        for i in range(1, length):
            if s[i] == '?':
                if s[i-1] != 'a':
                    s[i] = 'a'
                else:
                    s[i] = 'b'
            else:
                if s[i] == s[i-1]:
                    if s[i-1] != 'a':
                        s[i] = 'a'
                    else:
                        s[i] = 'b'
        return ''.join(s)
    
"""
https://leetcode-cn.com/submissions/detail/105220841/

89 / 100 个通过测试用例
状态：解答错误

输入："j?qg??b"
输出："jaqgaba"
预期："jaqgacb"
"""
