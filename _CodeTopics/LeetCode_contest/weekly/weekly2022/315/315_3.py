class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        for k in range(num+1):
            if k + int(str(k)[::-1]) == num:
                return True
        return False
    
"""
https://leetcode.cn/submissions/detail/373425661/

258 / 258 个通过测试用例
状态：通过
执行用时: 3172 ms
内存消耗: 16.1 MB
"""
