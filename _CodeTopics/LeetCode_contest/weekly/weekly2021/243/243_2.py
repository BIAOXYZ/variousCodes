class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        
        length = len(n)
        res = ''
        if n[0] != '-':
            for i in range(length):
                ch = n[i]
                if int(ch) >= x:
                    continue
                else:
                    res = n[:i] + str(x) + n[i:]
                    return res
            res = n + str(x)
            return res
        else:
            for i in range(1, length):
                ch = n[i]
                if int(ch) <= x:
                    continue
                else:
                    res = n[:i] + str(x) + n[i:]
                    return res
            res = n + str(x)
            return res
    
"""
https://leetcode-cn.com/submissions/detail/182116938/

97 / 97 个通过测试用例
状态：通过
执行用时: 268 ms
内存消耗: 18.4 MB
"""
