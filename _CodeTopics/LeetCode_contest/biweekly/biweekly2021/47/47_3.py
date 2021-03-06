class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        res = 0
        for i in range(length-2):
            ctr = collections.Counter(s[i:i+3])
            res += max(ctr.values()) - min(ctr.values())
            ##print s[i:i+3]
            for j in range(min(i+4, length+1), length+1):
                ctr[s[j-1]] = ctr.setdefault(s[j-1], 0) + 1
                res += max(ctr.values()) - min(ctr.values())
                ##print s[i:i+3], '--', s[i:j]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/151917464/

57 / 57 个通过测试用例
状态：通过
执行用时: 2128 ms
内存消耗: 12.9 MB
"""
