class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        lis = list(map(int, list(s)))
        lis.sort()
        return lis[0]*10 + lis[1]*10 + lis[2] + lis[3]
    
"""
https://leetcode-cn.com/submissions/detail/265022560/

99 / 99 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 13 MB
"""
