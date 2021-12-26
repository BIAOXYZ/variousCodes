class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        
        m = len(s)
        dic = {'L':[0,-1], 'R':[0,1], 'U':[-1,0], 'D':[1,0]}
        res = [-1] * m
        
        def is_legal(x, y):
            return 0 <= x < n and 0 <= y < n
        
        for i in range(m):
            j = i
            nextx, nexty = startPos[0] + dic[s[j]][0], startPos[1] + dic[s[j]][1]
            ##print s[j], dic[s[j]], nextx, nexty
            while j < m and is_legal(nextx, nexty):
                j += 1
                if j < m:
                    nextx, nexty = nextx + dic[s[j]][0], nexty + dic[s[j]][1]
            res[i] = j - i
        return res
    
"""
https://leetcode-cn.com/submissions/detail/252088367/

113 / 113 个通过测试用例
状态：通过
执行用时: 1740 ms
内存消耗: 13.4 MB
"""
