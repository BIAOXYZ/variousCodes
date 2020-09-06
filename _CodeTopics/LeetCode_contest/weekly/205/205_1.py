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
                    # 此时s[i-1]只能是从问号变过来的。
                    s[i-1] = 'c'
        return ''.join(s)
    
"""
https://leetcode-cn.com/submissions/detail/105224224/

100 / 100 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 12.7 MB
"""
