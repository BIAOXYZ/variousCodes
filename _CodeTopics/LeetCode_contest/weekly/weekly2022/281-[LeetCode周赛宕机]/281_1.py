class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        res = 0
        for i in range(2, num+1):
            lis = map(int, list(str(i)))
            if sum(lis) & 1 == 0:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/270589104/

71 / 71 个通过测试用例
状态：通过
执行用时: 48 ms
内存消耗: 12.9 MB
"""
