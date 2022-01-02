class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dic = collections.defaultdict(list)
        for i, ch in enumerate(s):
            dic[ch].append(i)
        
        if not dic['a'] or not dic['b']:
            return True
        return max(dic['a']) < min(dic['b'])
    
"""
https://leetcode-cn.com/submissions/detail/254157901/

216 / 216 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13 MB
"""
