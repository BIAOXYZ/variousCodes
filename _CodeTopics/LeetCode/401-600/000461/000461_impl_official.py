class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # 参考官方，主要区别就是while循环里不用除法之类的数学运算了，都用位运算代替。

        """
        # 000461.py代码

        res = 0
        tmp = x ^ y
        while tmp:
            if tmp % 2 != 0:
                res += 1
                tmp = (tmp - 1) / 2
            else:
                tmp /= 2
        return res
        """

        res = 0
        tmp = x ^ y
        while tmp:
            res += tmp & 1
            tmp >>= 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/181183385/

149 / 149 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.2 MB

执行用时：24 ms, 在所有 Python 提交中击败了28.48%的用户
内存消耗：13.2 MB, 在所有 Python 提交中击败了5.35%的用户
"""
"""
对比 000461.py 并没有快，所以是不是可以说明 000461.py 里的算术运算其实很快就（在计算机内部的运算中）进入了移位操作阶段？
"""
