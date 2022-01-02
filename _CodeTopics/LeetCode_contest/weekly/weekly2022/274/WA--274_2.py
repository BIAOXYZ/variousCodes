class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        
        m, n = len(bank), len(bank[0])
        if m <= 2:
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
https://leetcode-cn.com/submissions/detail/254167481/

143 / 145 个通过测试用例
状态：解答错误

最后执行的输入：
["1","1"]
"""
