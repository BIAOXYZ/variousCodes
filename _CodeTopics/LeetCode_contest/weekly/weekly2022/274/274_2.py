class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        
        m, n = len(bank), len(bank[0])
        if m < 2:
            return 0
        
        lights = [row.count('1') for row in bank]
        res = 0
        i = 0
        while i < m-1:
            if lights[i] == 0:
                i += 1
                continue
            j = i+1
            while j < m and lights[j] == 0:
                j += 1
            if j == m:
                break
            res += lights[i] * lights[j]
            i = j
        return res
    
"""
https://leetcode-cn.com/submissions/detail/254168296/

145 / 145 个通过测试用例
状态：通过
执行用时: 52 ms
内存消耗: 15.3 MB
"""
