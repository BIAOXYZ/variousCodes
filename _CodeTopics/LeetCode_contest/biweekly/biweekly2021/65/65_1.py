class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        ctr1 = collections.Counter(word1)
        ctr2 = collections.Counter(word2)
        l = [chr(i) for i in range(97, 123)]
        for k in l:
            n1 = ctr1.get(k, 0)
            n2 = ctr2.get(k, 0)
            if abs(n1 - n2) > 3:
                return False
        return True
    
"""
https://leetcode-cn.com/submissions/detail/238343521/

195 / 195 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.3 MB
"""
