class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        """
        # 先利用python的特性“投机取巧”一把：直接把字符串转成数字求和再转回字符串。
        """
        
        # 其实这里int函数按二进制转也是浪费，因为一求和，结果res还是十进制。
        numa = int(a,2)
        numb = int(b,2)
        res = numa + numb
        # 这里是因为python十进制转二进制后前面会多了0b，比如：
        # bin(5) 的结果是 0b101，所以要把最前面的0b去掉。
        return str(bin(res))[2:]
        
"""
https://leetcode-cn.com/submissions/detail/81327279/

294 / 294 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：12.7 MB
"""
