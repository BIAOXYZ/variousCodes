class Solution(object):
    def memLeak(self, memory1, memory2):
        """
        :type memory1: int
        :type memory2: int
        :rtype: List[int]
        """
        
        res = [1, memory1, memory2]
        i = 1
        while res[1] >= i or res[2] >= i:
            if res[1] >= res[2]:
                res = [i+1, res[1]-i, res[2]]
            else:
                res = [i+1, res[1], res[2]-i]
            i += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177805307/

82 / 82 个通过测试用例
状态：通过
执行用时: 364 ms
内存消耗: 13 MB
"""
