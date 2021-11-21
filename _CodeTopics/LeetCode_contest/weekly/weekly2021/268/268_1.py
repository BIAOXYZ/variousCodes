class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        
        n = len(colors)
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if colors[i] != colors[j]:
                    res = max(res, j-i)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/240696861/

126 / 126 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 12.9 MB
"""
