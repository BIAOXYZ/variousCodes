class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        a, b = str(bin(a))[2:], str(bin(b))[2:]
        a = a[::-1]
        b = b[::-1]
        
        s = ''
        incr = '0'
        for i in range(max(len(a), len(b))):
            ai = a[i] if i < len(a) else '0'
            bi = b[i] if i < len(b) else '0'
            tmp = ai + bi + incr
            if tmp.count('1') == 0:
                s += '0'; incr = '0'
            elif tmp.count('1') == 1:
                s += '1'; incr = '0'
            elif tmp.count('1') == 2:
                s += '0'; incr = '1'
            else:
                s += '1'; incr = '1'
        if incr == '1':
            s += '1'
        return int(s[::-1], 2)
        
"""
https://leetcode-cn.com/submissions/detail/223225013/

10 / 13 个通过测试用例
状态：解答错误

最后执行的输入：
-1
1
输出：
2
预期结果：
0
"""
