class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        
        se = set()
        for x, y in dig:
            se.add(n*x + y)
        
        res = 0
        for coor in artifacts:
            satisfyFlag = True
            x1, y1, x2, y2 = coor
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    satisfyFlag = satisfyFlag and (n*x + y in se)
            if satisfyFlag:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/282164862/

97 / 97 个通过测试用例
状态：通过
执行用时: 232 ms
内存消耗: 56.9 MB
"""
