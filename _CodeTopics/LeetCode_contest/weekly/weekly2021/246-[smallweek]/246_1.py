class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ''
    
"""
https://leetcode-cn.com/submissions/detail/188122428/

196 / 196 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 17.6 MB
"""
