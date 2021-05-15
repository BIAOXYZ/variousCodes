class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        lis = s.split()
        
        dic = {}
        for word in lis:
            dic[int(word[-1])] = word[:-1]
        
        res = ""
        for i in range(1, len(lis)+1):
            res += dic[i] + " "
        return res[:-1]
    
"""
https://leetcode-cn.com/submissions/detail/177801594/

45 / 45 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
