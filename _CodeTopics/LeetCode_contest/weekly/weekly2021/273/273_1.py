class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        s = str(num)
        r1 = str(int(s[::-1]))
        r2 = int(r1[::-1])
        return num == r2
    
"""
https://leetcode-cn.com/submissions/detail/252080120/

129 / 129 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 12.9 MB
"""
