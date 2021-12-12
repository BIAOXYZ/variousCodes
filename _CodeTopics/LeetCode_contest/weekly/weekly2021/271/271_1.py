class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        
        n = len(rings)
        dic = {}
        for i in range(1, n, 2):
            num = rings[i]
            color = rings[i-1]
            if num in dic:
                dic[num].add(color)
            else:
                dic[num] = set([color])
        res = 0
        for v in dic.values():
            if len(v) == 3:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/247636355/

66 / 66 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.9 MB
"""
