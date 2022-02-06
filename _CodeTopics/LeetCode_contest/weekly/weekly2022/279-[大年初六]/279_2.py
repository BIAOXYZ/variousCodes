class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num == 0:
            return num
        isNegtive = False
        if num < 0:
            isNegtive = True
            num = -num
        
        lis = list(map(int, list(str(num))))
        lis.sort()
        print lis
        if isNegtive:
            return -int(''.join(map(str, reversed(lis))))
        i = 0
        while lis[i] == 0:
            i += 1
        return int(str(lis[i]) + '0'*i + ''.join(map(str, lis[i+1:])))
    
"""
https://leetcode-cn.com/submissions/detail/265107720/

413 / 413 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.3 MB
"""
