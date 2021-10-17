class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = s.split()
        tmp = []
        for token in l:
            if token[0].isdigit():
                tmp.append(int(token))
        return tmp == sorted(list(set(tmp)))
    
"""
https://leetcode-cn.com/submissions/detail/229582321/

97 / 97 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.3 MB
"""
