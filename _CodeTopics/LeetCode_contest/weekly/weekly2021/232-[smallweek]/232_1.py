class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        ind = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ind.append(i)
                if len(ind) > 2:
                    return False
        if not ind or (len(ind) == 2 and s1[ind[0]] == s2[ind[1]] and s1[ind[1]] == s2[ind[0]]):
            return True
        return False
    
"""
https://leetcode-cn.com/submissions/detail/154892646/

113 / 113 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 13.1 MB
"""
