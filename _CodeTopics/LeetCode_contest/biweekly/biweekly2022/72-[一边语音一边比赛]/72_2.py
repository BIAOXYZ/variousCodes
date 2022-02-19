class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        if num % 3 != 0:
            return []
        return [num/3 - 1, num/3, num/3 + 1]
    
"""
https://leetcode-cn.com/submissions/detail/270473248/

379 / 379 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13.1 MB
"""
