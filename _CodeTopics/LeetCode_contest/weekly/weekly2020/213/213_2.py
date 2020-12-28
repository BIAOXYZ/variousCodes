class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        res = [1,1,1,1,1]
        for round in range(n-1):
            res[1] += res[0]
            res[2] += res[1]
            res[3] += res[2]
            res[4] += res[3]
        return sum(res)
    
"""
https://leetcode-cn.com/submissions/detail/120110471/

41 / 41 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 13 MB
"""
