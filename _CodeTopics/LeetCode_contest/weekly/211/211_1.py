class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        dic = {}
        for i in range(length):
            if dic.has_key(s[i]):
                dic[s[i]].append(i)
            else:
                dic[s[i]] = [i]
        
        res = -1
        for value in dic.values():
            if len(value) >= 2:
                res = max(res, value[-1]-value[0]-1)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/116578019/

54 / 54 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB
"""
