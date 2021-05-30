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
                if int(ch) > x:
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
https://leetcode-cn.com/submissions/detail/182115903/

90 / 97 个通过测试用例
状态：解答错误

最后执行的输入：
"469975787943862651173569913153377"
3
"""
