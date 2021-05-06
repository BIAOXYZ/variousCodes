class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        # 参考答案和其他分析，主要思想是把对结果的计算分成两部分：最低位和其他位。
        # 总体而言算是毕竟难想的解法。
        
        def sumXor(x):
            if x % 4 == 0:
                return x
            elif x % 4 == 1:
                return 1
            elif x % 4 == 2:
                return x + 1
            else:
                return 0
        
        s = start >> 1
        e = n & start & 1
        res = (sumXor(s - 1) ^ sumXor(s + n - 1)) 
        return res << 1 | e
        
"""
https://leetcode-cn.com/submissions/detail/174974138/

54 / 54 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 12.8 MB

执行用时：8 ms, 在所有 Python 提交中击败了99.64%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了89.68%的用户
"""
