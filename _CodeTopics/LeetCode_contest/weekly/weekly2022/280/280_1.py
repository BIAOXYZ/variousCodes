class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
        step = 0
        while num1 > 0 and num2 > 0:
            step += 1
            big, small = max(num1, num2), min(num1, num2)
            num1, num2 = small, big - small
        return step
    
"""
https://leetcode-cn.com/submissions/detail/267659712/

161 / 161 个通过测试用例
状态：通过
执行用时: 172 ms
内存消耗: 12.9 MB
"""
