class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        
        special.sort()
        res = 0
        start = bottom
        for i in range(len(special)):
            end = special[i]
            res = max(res, end - start)
            start = end + 1
        res = max(res, top - start + 1)
        return res
    
"""
https://leetcode.cn/submissions/detail/313654871/

80 / 80 个通过测试用例
状态：通过
执行用时: 192 ms
内存消耗: 21 MB
"""
