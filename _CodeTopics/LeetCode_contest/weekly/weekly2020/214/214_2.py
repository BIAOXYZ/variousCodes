class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {}
        for ch in s:
            if dic.has_key(ch):
                dic[ch] += 1
            else:
                dic[ch] = 1
        
        dic2, lis = {}, dic.values()
        res = 0
        for frequence in lis:
            if dic2.has_key(frequence):
                frequence -= 1
                res += 1
                while frequence > 0 and dic2.has_key(frequence):
                    frequence -= 1
                    res += 1
                if frequence > 0:
                    dic2[frequence] = True
            else:
                dic2[frequence] = True
        return res
    
"""
https://leetcode-cn.com/submissions/detail/121820388/

103 / 103 个通过测试用例
状态：通过
执行用时: 244 ms
内存消耗: 13.6 MB
"""
