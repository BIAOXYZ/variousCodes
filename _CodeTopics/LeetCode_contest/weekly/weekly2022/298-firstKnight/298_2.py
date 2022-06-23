class Solution(object):
    def minimumNumbers(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        
        if num == 0:
            return 0
        for i in range(1, 11):
            if k * i % 10 == num % 10 and k * i <= num:
                return i
        return -1
    
"""
https://leetcode.cn/submissions/detail/326790372/

298 / 298 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13 MB
"""
